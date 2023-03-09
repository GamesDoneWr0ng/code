import numpy as np
from Network import Network

class PPO:
    def __init__(self, actor: Network, scoreRequierment, clippingThreshold = 0.2):
        self.trajectories = []
        self.actor = actor
        self.oldActor = actor
        self.critic = Network(actor.size[0], actor.size[1,-1], 1)
        self.scoreRequierment = scoreRequierment
        self.clippingThreshold = clippingThreshold

    def loss_CategoricalCrossentropy(self, Y_pred, Y_true):
        samples = len(Y_pred)
        y_pred_clipped = np.clip(Y_pred, 1e-7, 1-1e-7)

        if len(Y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), Y_true]
        else:
            correct_confidences = np.sum(y_pred_clipped*Y_true, axis=1)

        negative_log_likelihoods = -np.log(correct_confidences)

        data_loss = np.mean(negative_log_likelihoods)
        return data_loss

    def value(self, states: np.ndarray, reward: float):
        reward = reward / self.scoreRequierment
        Y_pred = self.critic.run(states)
        Y_true = np.zeros_like(Y_pred) + reward
        loss = self.loss_CategoricalCrossentropy(Y_pred, Y_true)

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
        surrogate1 = ratio * advantages
        surrogate2 = clip_ratio * advantages
        return np.sum(np.minimum(surrogate1, surrogate2), axis=0)
        #return -np.mean(np.minimum(surrogate1, surrogate2))

    def runNetwork(self, inputs):
        # store trajectory (state, action taken, reward, next state)
        outputs = self.network.run(inputs)
        return outputs

    def howToRun(self):
        inputs = [1,2,3,4]
        oldChance = np.max(self.oldActor.run(inputs))
        newChance = np.max(self.actor.run(inputs))
        self.clipped_surrogate_objective(oldChance, newChance, [])


"""inputs from snake
16 lines out of snake head (distance to colistion / max distance)
16 inputs for what the lines hit (-1 wall, 0 snake, 1 apple)
2 for head position
2 for relative position to apple
2 for relative position to tail
"""
