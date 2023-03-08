import numpy as np
from Network import Network

# The AI plays for one batch (32 moves)
# It return the trajectories

class PPO:
    def __init__(self, actor, clippingThreshold = 0.2):
        self.trajectories = []
        self.actor = actor
        self.critic = Network(actor.size[0], [actor.size[1:-1]], 1)
        self.clippingThreshold = clippingThreshold

    def generalized_advantage_estimate(value_old_state, value_new_state, reward, done, gamma=0.99, lamda=0.95):
        """
        Get generalized advantage estimate of a trajectory
        value_old_state: value function result with old_state input
        value_new_state: value function result with new_state input
        reward: agent reward of taking actions in the environment
        done: flag for end of episode
        gamma: trajectory discount (scalar) 0.99
        lamda: exponential mean discount (scalar) 0.95
        """
        batch_size = done.shape[0]

        advantage = np.zeros(batch_size + 1)

        for t in reversed(range(batch_size)):
            delta = reward[t] + (gamma * value_new_state[t] * done[t]) - value_old_state[t]
            advantage[t] = delta + (gamma * lamda * advantage[t + 1] * done[t])

        value_target = advantage[:batch_size] + np.squeeze(value_old_state)

        return advantage[:batch_size], value_target

    def runNetwork(self, inputs):
        # store trajectory (state, action taken, reward, next state)
        outputs = self.network.activate(inputs)
        return outputs