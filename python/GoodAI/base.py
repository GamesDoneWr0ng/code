import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

name = "base"

def make_env(gym_id = "InvertedDoublePendulum-v4"):
    env = gym.make(gym_id)
    return env

vec_env = make_vec_env(make_env, n_envs=4)

#model = PPO.load(f"python/GoodAI/policies/{name}")

model = PPO("MlpPolicy", vec_env, verbose=1, ent_coef=0.02, gamma=0.99, device="auto", tensorboard_log=f"./python/GoodAI/runs/ppo_{name}/")
model.learn(total_timesteps=1000000, progress_bar=True, tb_log_name="run")
 
model.save(f"python/GoodAI/policies/{name}")

obs = vec_env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render("human")