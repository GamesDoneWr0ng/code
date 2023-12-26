import numpy as np
import pygame as pg
import gymnasium as gym
from gymnasium import spaces
import chess

class ChessEnv(gym.Env):
    def __init__(self):
        metadata = {"render_modes": ["human", "rgb_array"]}
        # The action will be a single continuous value representing the evaluation of the board
        self.action_space = spaces.Box(low=-np.inf, high=np.inf, shape=(1,))

        # 8*8 grid * 12 posible pices + whos turn + castles + en pasant
        self.observation_space = spaces.Box(low=0, high=1, shape=(9,), dtype=np.uint8)

        self.board = chess.Board()

        self._get_obs()

    def _get_obs(self):
        obs = np.zeros((8*8 * 12 + 1+4+16))
        for i, piece in enumerate(self.board.piece_map().values()):
            obs[i*8*8:(i+1)*8*8] = np.array(pg.surfarray.pixels3d(piece.image))
        obs[-8*8:] = np.array(pg.surfarray.pixels3d(self.board.turn_indicator))
        obs[-8*8-1:-8*8] = self.board.castling_rights
        obs[-8*8-2:-8*8-1] = self.board.ep_square
        return obs
    

env = ChessEnv()