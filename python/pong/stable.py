import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.atari_wrappers import MaxAndSkipEnv

gym.register( # register the environment
    id='Pong-v0',
    entry_point='pong:PongEnv')

def make_env(gym_id = "Pong-v0"):
    env = gym.make(gym_id)
    env = MaxAndSkipEnv(env, skip=4)
    return env

vec_env = make_vec_env(make_env, n_envs=4)

model = PPO.load("python/pong/policies/stablebase")

model = PPO("MlpPolicy", vec_env, verbose=1, ent_coef=0.02, gamma=0.95, device="auto", tensorboard_log="./python/pong/runs/ppo_pong_tensorboard/")
model.learn(total_timesteps=1000000, progress_bar=True, tb_log_name="run")
 
#model.save("python/pong/policies/stablebase")

obs = vec_env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render("human")