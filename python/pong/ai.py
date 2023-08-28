import argparse
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = "TRUE"
from distutils.util import strtobool
import gymnasium as gym
import time
import random
import numpy as np
import torch

gym.register( # register the environment
    id='Pong-v0',
    entry_point='python.pong.pong:PongEnv')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--exp-name', type=str, default=os.path.basename(__file__).rstrip(".py"),
                        help='the name of this experiment')
    parser.add_argument('--gym-id', type=str, default='Pong-v0',
                        help='the id of the gym environment')
    parser.add_argument('--learning-rate', type=float, default=2.5e-4,
                        help='the learning rate of the optimizer')
    parser.add_argument('--seed', type=int, default=1,
                        help='seed of the experiment')
    parser.add_argument('--total-timesteps', type=int, default=40000000,
                        help='total timesteps of the experiments')
    parser.add_argument('--torch-deterministic', type=lambda x:bool(strtobool(x)), default=True, nargs='?', const=True,
                        help='if toggled, `torch.backends.cudnn.deterministic=False`')
    parser.add_argument('--cuda', type=lambda x:bool(strtobool(x)), default=True, nargs='?', const=True,
                        help='if toggled, cuda will not be enabled by default')
    parser.add_argument('--track', type=lambda x:bool(strtobool(x)), default=False, nargs='?', const=True,
                        help='if toggled, this experiment will be tracked with Weights and Biases')
    parser.add_argument('--wandb-project-name', type=str, default="cleanRL",
                        help="the wandb's project name")
    parser.add_argument('--wandb-entity', type=str, default=None,
                        help="the entity (team) of wandb's project")
    args = parser.parse_args()
    return args

args = parse_args()
print(args)
run_name = f"{args.gym_id}__{args.exp_name}__{args.seed}__{int(time.time())}"

if args.track:
    import wandb
    wandb.init(
        project=args.wandb_project_name,
        entity=args.wandb_entity,
        sync_tensorboard=False,
        config=vars(args),
        name=run_name,
        monitor_gym=True,
        save_code=True
    )

# TRY NOT TO MODIFY: seeding
random.seed(args.seed)
np.random.seed(args.seed)
torch.manual_seed(args.seed)
torch.backends.cudnn.deterministic = args.torch_deterministic

device = torch.device("cuda" if torch.cuda.is_available() and args.cuda else "cpu")

def make_env(gym_id):
    def thunk():
        env = gym.make(gym_id)
        env = gym.wrappers.RecordEpisodeStatistics(env)
        env = gym.wrappers.RecordVideo(env, "python/pong/videos", episode_trigger = lambda t: t % 100 == 0)
        return env
    return thunk

envs = gym.vector.SyncVectorEnv([make_env(args.gym_id)])
observation = envs.reset()
for _ in range(200):
    action = envs.action_space.sample()
    observation, reward, done, info = envs.step(action)
    for item in info:
        if "episode" in item.keys:
            print(f"episodic_return: {item['episode']['r']}")