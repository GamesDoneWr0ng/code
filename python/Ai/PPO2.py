from Network import Network
import numpy as np

# standard loss function and its derivative
def mse(y_true, y_pred):
    return np.mean(np.power(y_true-y_pred, 2))

def mse_prime(y_true, y_pred):
    return 2*(y_pred-y_true)/y_true.size

class PPO:
    def __init__(self, actor: Network, loss = mse, loss_prime = mse_prime, c1=0.5,c2=0.01):
        self.actor = actor
        self.oldActor = actor
        self.critic = Network(actor.size[0], actor.size[1:-1], 1)

        self.batchSize = 32

        self.lossF = loss
        self.loss_prime = loss_prime
        self.c1 = c1
        self.c2 = c2

# caluclate the discontedSumOfRewards from the rewards and done array
    def discountedSumOfRewards(self, rewards, done, gamma=0.95):
        sums = []
        discounted_reward = 0
        for reward, is_terminal in zip(reversed(rewards), reversed(done)):
            if is_terminal:
                discounted_reward = 0
            discounted_reward = reward + (gamma * discounted_reward)
            sums.insert(0, discounted_reward)
        return np.array(sums)

# forward pass of the network
    def runNetwork(self, inputs):
        outputs = self.actor.forward(inputs)
        return outputs

# lenght of states will allways be equal to batchSize to avoid to big policy updates
    def train(self, states, actions, rewards, done):
        # update old actor
        self.oldActor = self.actor

        # calculate the discounted sum of rewards
        discounted_rewards = self.discountedSumOfRewards(rewards, done)

        # calculate the value of the states
        values = self.critic.forward(states).flatten()

        # calculate the advantages
        advantages = discounted_rewards - values[1:]

        for state, action, advantage in zip(states, actions, advantages):
            # do a forward pass of the actor network
            probs = self.runNetwork(state)
            print(probs)

            ratio = probs.flatten() / self.oldActor.forward(state).flatten()
            surr1 = ratio * advantage
            surr2 = np.clip(ratio, 1 - 0.2, 1 + 0.2) * advantage
            loss = -np.mean(np.minimum(surr1, surr2)) # probably change something here future me
            loss /= self.batchSize

            # maybe full loss function with entropy and value function later

            # update the actor network
            self.actor.backward(loss, learning_rate = 0.01)
        
        # update the critic network
        self.critic.fit(states[1:], discounted_rewards, 10, self.loss_prime, learning_rate=0.01)