import numpy as np
import pygame as pg
import gymnasium as gym
from gymnasium import spaces

class PongEnv:
    metadata = {"render_modes": ["human-vs-bot", "training"], "render_fps": 4}

    def __init__(self, size, render_mode=None) -> None:
        self.size = size
        self.score = [0,0]
        self.reset()

        # Observations are dictionaries with the agent's and the target's location.
        # Each location is encoded as an element of {0, ..., `size`}^2, i.e. MultiDiscrete([size, size]).
        self.observation_space = spaces.Dict(
            {
                "ballPos": spaces.Discrete(2),
                "ballVel": spaces.Discrete(2),
                "Paddles": spaces.Discrete(2)
            }
        )

        # We have 2 actions, corresponding to "up", "down"
        self.action_space = spaces.Discrete(2)

        self._action_to_direction = {
            0: -1,
            1: 1
        }

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        """
        If human-vs-bot is used, `self.window` will be a reference
        to the window that we draw to. `self.clock` will be a clock that is used
        to ensure that the environment is rendered at the correct framerate in
        human-mode. They will remain `None` until human-mode is used for the
        first time.
        """
        self.window = None
        self.clock = None

    def _get_obs(self):
        return {
            "ballPos": self.ballPos,
            "ballVel": self.ballVel,
            "Paddles": [self.aiPaddle, self.playerPaddle]
        }
    
    def _get_info(self):
        return {
            "score": self.score
        }

    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        self.ballPos = np.array(self.size) / 2
        self.ballVel = np.random.randn(2) # Randomize velocity
        self.ballVel = 2 * self.ballVel / np.sqrt(np.sum(self.ballVel**2)) # normalize the velocity
        self.aiPaddle     = self.size[1] / 2
        self.playerPaddle = self.size[1] / 2

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, info

    def step(self, human, action):
        direction = self._action_to_direction[action]
        reward = 0

        # player input
        self.playerPaddle = np.clip(self.playerPaddle + human, 50, self.size[1] - 50)
        self.ballPos += self.ballVel
        
        # bounce off top and bottom
        if self.ballPos[1] < 10 and self.ballVel[1] < 0 or self.ballPos[1] > self.size[1] - 10 and self.ballVel[1] > 0:
            self.ballVel[1] *= -1

        # bounce off paddles
        ballRect = pg.Rect(self.ballPos[0] - 10, self.ballPos[1] - 10, 20, 20)
        aiPaddleRect = pg.Rect(50, self.aiPaddle - 50, 10, 100)
        playerPaddleRect = pg.Rect(self.size[0] - 50, self.playerPaddle - 50, 10, 100)

        if self.ballVel[0] > 0:
            if ballRect.colliderect(playerPaddleRect):
                self.ballVel[0] *= -1.2
                differenece = self.ballPos[1] - self.playerPaddle
                self.ballVel[1] += differenece / 30

                # normalize
                speed = np.sqrt(np.sum(self.ballVel**2))
                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2)) * speed
        else:
            if ballRect.colliderect(aiPaddleRect):
                self.ballVel[0] *= -1.2
                differenece = self.ballPos[1] - self.aiPaddle
                self.ballVel[1] += differenece / 100

                # normalize
                speed = np.sqrt(np.sum(self.ballVel**2))
                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2)) * speed

                reward = 2

        # gain points
        if self.ballPos[0] > self.size[0]:
            self.score[0] += 1
            self.reset()
            terminated = True
            reward = 1
        elif self.ballPos[0] < 0:
            self.score[1] += 1
            self.reset()
            terminated = True
            reward = -1

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, reward, terminated, False, info
    
    def render(self):
        if self.render_mode == "training":
            return self._render_frame()
        
    def _render_frame(self):
        if self.window is None and self.render_mode == "human-vs-bot":
            pg.init()
            pg.display.init()
            self.window = pg.display.set_mode(self.size)
        if self.clock is None and self.render_mode == "human-vs-bot":
            self.clock = pg.time.Clock()

        canvas = pg.Surface((self.window_size, self.window_size))

        canvas.fill((0,0,0))
        pg.draw.rect(canvas, (255,255,255), (self.ballPos[0] - 10, self.ballPos[1] - 10, 20, 20))
        pg.draw.rect(canvas, (255,255,255), (45, self.aiPaddle - 50, 10, 100))
        pg.draw.rect(canvas, (255,255,255), (self.size[0] - 45, self.playerPaddle - 50, 10, 100))

        font = pg.font.SysFont('didot.ttc', 50)
        img = font.render(str(self.score[0]), True, (255,255,255))
        canvas.blit(img, (0, 0))

        img = font.render(str(self.score[1]), True, (255,255,255))
        canvas.blit(img, (self.size[0] - img.get_width(), 0))

        if self.render_mode == "human":
            # The following line copies our drawings from `canvas` to the visible window
            self.window.blit(canvas, canvas.get_rect())
            pg.event.pump()
            pg.display.update()

            # We need to ensure that human-rendering occurs at the predefined framerate.
            # The following line will automatically add a delay to keep the framerate stable.
            self.clock.tick(self.metadata["render_fps"])
        else:  # rgb_array
            return np.transpose(
                np.array(pg.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
            )
        
    def close(self):
        if self.window is not None:
            pg.display.quit()
            pg.quit()