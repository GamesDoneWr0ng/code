import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

name = "Snake2"

gym.register( # register the environment
    id='Snake-v0',
    entry_point='envs.snake:SnakeEnv')

vec_env = make_vec_env("Snake-v0", n_envs=4)

model = PPO.load(f"python/GoodAI/policies/{name}", env=vec_env)

model = PPO("MlpPolicy", vec_env, verbose=1, ent_coef=0.01, tensorboard_log=f"./python/GoodAI/runs/ppo_{name}/")
model.learn(total_timesteps=9_000_000, progress_bar=True, tb_log_name="run")

#model.save(f"python/GoodAI/policies/{name}")

obs = vec_env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render("human")