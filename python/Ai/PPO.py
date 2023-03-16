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

    def generalized_advantage_estimate(self, value_old_state, value_new_state, reward, done, gamma=0.99, lamda=0.95):
        """
        Get generalized advantage estimate of a trajectory
        value_old_state: value function result with old_state input
        value_new_state: value function result with new_state input
        reward: agent reward of taking actions in the environment
        done: flag for end of episode
        gamma: trajectory discount (scalar) = 0.99
        lamda: exponential mean discount (scalar) = 0.95
        """
        batch_size = done.shape[0]

        advantage = np.zeros(batch_size + 1)

        for t in reversed(range(batch_size)):
            delta = reward[t] + (gamma * value_new_state[t] * done[t]) - value_old_state[t]
            advantage[t] = delta + (gamma * lamda * advantage[t + 1] * done[t])

        value_target = advantage[:batch_size] + np.squeeze(value_old_state)

        return advantage[:batch_size], value_target

    def clipped_surrogate_objective(self, old_policy, new_policy, advantages):
        """
        Calculates the clipped surrogate objective function for PPO.
        Epsilon = self.clippingThreshold = 0.2
        """
        ratio = new_policy / old_policy
        clip_ratio = np.clip(ratio, 1 - self.clippingThreshold, 1 + self.clippingThreshold)
        surrogate1 = ratio.T * advantages
        surrogate2 = clip_ratio.T * advantages
        return np.sum(np.minimum(surrogate1, surrogate2), axis=0)

    def runNetwork(self, inputs):
        # store trajectory (state, action taken, reward, next state)
        outputs = self.actor.forward(inputs)
        return outputs

    def train(self, states, rewards):
        values = np.array([0]) + [self.critic.forward(i) for i in states] + [np.sum(rewards)]
        done = np.array([0 for _ in rewards[1:]] + np.array([1]))
        advantages, value_target = self.generalized_advantage_estimate(values[:-1], values[1:], rewards, done)
        error = self.clipped_surrogate_objective(self.oldActor.forward(states[1:]), self.actor.forward(states[1:]), advantages)
        self.actor.backward(error)
