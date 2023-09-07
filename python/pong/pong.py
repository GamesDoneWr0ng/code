import numpy as np
import pygame as pg
import gymnasium as gym
from gymnasium import spaces

class PongEnv(gym.Env):
    metadata = {"render_modes": ["human-vs-bot", "training", "rgb_array"], "render_fps": 60}

    def __init__(self, size = [800,600], render_mode="rgb_array") -> None:
        self.size = size
        self.score = [0,0]
        self.reset()

        high = np.array(
            [
                self.size[0] + 50,
                self.size[1] + 50,
                np.finfo(np.float32).max,
                np.finfo(np.float32).max,
                self.size[1],
                self.size[1],
            ]
        )

        low = np.array(
            [
                -50,
                -50,
                -np.finfo(np.float32).max,
                -np.finfo(np.float32).max,
                0,
                0,
            ]
        )

        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=low, high=high, dtype=np.float32)

        self._action_to_direction = {
            0: -4,
            1: 4
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
        return np.array([
            self.ballPos[0], self.ballPos[1],
            self.ballVel[0], self.ballVel[1], 
            self.aiPaddle, self.playerPaddle
        ], dtype=np.float32)

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

        if self.render_mode == "human-vs-bot":
            self._render_frame()

        return observation, info

    def step(self, action = 0, human = 0):
        if abs(self.ballVel[0]) < 1:
            self.ballVel[0] = np.sign(self.ballVel[0])

        direction = self._action_to_direction[action]
        reward = 0

        # move ai paddle
        self.aiPaddle += direction

        # player input
        if self.render_mode == "human-vs-bot":
            self.playerPaddle = np.clip(self.playerPaddle + human, 50, self.size[1] - 50)
        else:
            if self.ballPos[1] > self.playerPaddle:
                self.playerPaddle += 4
            else:
                self.playerPaddle -= 4
        
        self.ballPos += self.ballVel
        self.aiPaddle = np.clip(self.aiPaddle, 50, self.size[1] - 50)
        
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
                speed = np.sqrt(np.sum(self.ballVel**2))
                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2))
                differenece = self.ballPos[1] - self.playerPaddle
                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2))
                self.ballVel[1] += differenece / 30

                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2)) * speed
        else:
            if ballRect.colliderect(aiPaddleRect):
                self.ballVel[0] *= -1.2
                speed = np.sqrt(np.sum(self.ballVel**2))
                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2))
                differenece = self.ballPos[1] - self.playerPaddle
                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2))
                self.ballVel[1] += differenece / 30

                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2)) * speed

                reward += 1

        terminated = False
        # gain points
        if self.ballPos[0] > self.size[0]:
            self.score[0] += 2
            self.reset()
            terminated = True
            reward += 1
        elif self.ballPos[0] < 0:
            self.score[1] += 1
            reward -= 1 * (abs(self.aiPaddle - self.ballPos[1])) / 200
            self.reset()
            terminated = True

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human-vs-bot":
            self._render_frame()

        return observation, reward, terminated, False, info
    
    def render(self):
        if self.render_mode == "rgb_array" or self.render_mode == "human-vs-bot":
            return self._render_frame()

    def _render_frame(self):
        if self.window is None and self.render_mode == "human-vs-bot":
            pg.init()
            pg.display.init()
            self.window = pg.display.set_mode(self.size)
        if self.clock is None and self.render_mode == "human-vs-bot":
            self.clock = pg.time.Clock()

        pg.font.init()
        canvas = pg.Surface(self.size)

        canvas.fill((0,0,0))
        pg.draw.rect(canvas, (255,255,255), (self.ballPos[0] - 10, self.ballPos[1] - 10, 20, 20))
        pg.draw.rect(canvas, (255,255,255), (45, self.aiPaddle - 50, 10, 100))
        pg.draw.rect(canvas, (255,255,255), (self.size[0] - 45, self.playerPaddle - 50, 10, 100))

        font = pg.font.SysFont('didot.ttc', 50)
        img = font.render(str(self.score[0]), True, (255,255,255))
        canvas.blit(img, (0, 0))

        img = font.render(str(self.score[1]), True, (255,255,255))
        canvas.blit(img, (self.size[0] - img.get_width(), 0))

        if self.render_mode == "human-vs-bot":
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