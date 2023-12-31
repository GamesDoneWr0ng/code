import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.callbacks import BaseCallback
import numpy as np
import chess

# Define the order of the pieces in the observation array
PIECES = [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, chess.KING]

class UpdateModelCallback(BaseCallback):
    def __init__(self, vec_env, verbose=0):
        super(UpdateModelCallback, self).__init__(verbose)
        self.vec_env = vec_env

    def _on_step(self) -> bool:
        # This method is required by BaseCallback, but we don't use it.
        return True

    def on_rollout_start(self) -> bool:
        for env in self.vec_env.envs:
            env.env.env.env.model = self.model
        return True


if __name__=='__main__':
    name = "Chess"

    gym.register( # register the environment
        id='MyChess',
        entry_point='chessEnv:ChessEnv')

    vec_env = make_vec_env("MyChess", n_envs=1)

    model = PPO.load(f"python/GoodAI/policies/{name}", env=vec_env)

    #model = PPO("MlpPolicy", vec_env, verbose=1, ent_coef=0.01, tensorboard_log=f"./python/GoodAI/runs/ppo_{name}/")
    #callback = UpdateModelCallback(vec_env)
    #model.learn(total_timesteps=1_000_000, progress_bar=True, tb_log_name="run", callback=callback)

    #model.save(f"python/GoodAI/policies/{name}")

    for env in vec_env.envs:
        env.env.env.env.model = model

    obs = vec_env.reset()
    while True:
        obs, rewards, dones, info = vec_env.step((np.array([[1]]),None))
        for env in vec_env.envs:
            env.env.env.env._render_frame()