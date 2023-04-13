import numpy as np
from Network import Network

# standard loss function and its derivative
def mse(y_true, y_pred):
    return np.mean(np.power(y_true-y_pred, 2))

def mse_prime(y_true, y_pred):
    return 2*(y_pred-y_true)/y_true.size

class PPO:
    def __init__(self, actor: Network, maxScore, clippingThreshold = 0.2, loss = mse, loss_prime = mse_prime):
        self.trajectories = []
        self.actor = actor
        self.oldActor = actor
        self.critic = Network(actor.size[0], actor.size[1:-1], 1)
        self.maxScore = maxScore
        self.clippingThreshold = clippingThreshold
        self.loss = loss
        self.loss_prime = loss_prime

    def clipped_surrogate_objective(self, old_policy, new_policy, advantages):
        """
        Calculates the clipped surrogate objective function for PPO.
        Epsilon = self.clippingThreshold = 0.2
        """
        ratio = new_policy / old_policy
        clip_ratio = np.clip(ratio, 1 - self.clippingThreshold, 1 + self.clippingThreshold)
        surrogate1 = np.apply_along_axis(np.multiply, 0, ratio, advantages.T)
        surrogate2 = np.apply_along_axis(np.multiply, 0, clip_ratio, advantages.T)

        if np.any((ratio > 1+self.clippingThreshold)|(ratio < 1-self.clippingThreshold)):
            self.oldActor = self.actor

        return np.mean(np.minimum(surrogate1, surrogate2), axis=1)

    def discountedSumOfRewards(self, rewards, gamma=0.9):
        sums = []
        for _ in range(len(rewards)):
            sum = 0
            for index, i in enumerate(rewards[_:]):
                sum += i * gamma ** index
            sums.append(sum)
        return np.array(sums)

    def runNetwork(self, inputs):
        outputs = self.actor.forward(inputs)
        return outputs

    def train(self, states, rewards):
        expectedRewarwds = 50*((2 * np.array([self.critic.forward(i)[0][0] for i in states])) - 1)
        actualRewards = self.discountedSumOfRewards(rewards)
        advantages = actualRewards - expectedRewarwds

        # train critic
        self.critic.fit(states, actualRewards, 10, self.loss_prime, learning_rate=0.01)

        probs = self.actor.forward(states)
        clipped = self.clipped_surrogate_objective(self.oldActor.forward(states), probs, advantages)
        loss = np.average(expectedRewarwds)
        #entropy = -np.sum(np.log(probs), axis=1)

        loss = clipped - loss #+ entropy

        self.actor.backward(loss)
