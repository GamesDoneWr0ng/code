import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

gym.register( # register the environment
    id='Pong-v0',
    entry_point='pong:PongEnv')

vec_env = make_vec_env("Pong-v0", n_envs=4)

model = PPO("MlpPolicy", vec_env, verbose=1, ent_coef=0.02, gamma=0.95, device="auto")
model.learn(total_timesteps=500000, progress_bar=True)
model.save("stablebase")

obs = vec_env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render("human")