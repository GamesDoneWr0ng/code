import numpy as np
import math

class PPO:
    def __init__(self, actor, clippingThreshold = 0.2):
        self.trajectories = []
        self.actor = actor
        self.clippingThreshold = clippingThreshold

    def generalized_advantage_estimate(gamma: float, lamda: float, value_old_state, value_new_state, reward, done):
        """
        Get generalized advantage estimate of a trajectory
        gamma: trajectory discount (scalar)
        lamda: exponential mean discount (scalar)
        value_old_state: value function result with old_state input
        value_new_state: value function result with new_state input
        reward: agent reward of taking actions in the environment
        done: flag for end of episode
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