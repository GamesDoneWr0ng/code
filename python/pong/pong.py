import numpy as np
import pygame as pg
import gymnasium as gym
from gymnasium import spaces

class PongEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 60}

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
        If human is used, `self.window` will be a reference
        to the window that we draw to. `self.clock` will be a clock that is used
        to ensure that the environment is rendered at the correct framerate in
        human-mode. They will remain `None` until human-mode is used for the
        first time.
        """
        self.window = None
        self.clock = None

    def _get_obs(self):
        if self.ballVel[0] < 0:
            return np.array([
                self.ballPos[0], self.ballPos[1],
                self.ballVel[0], self.ballVel[1], 
                self.aiPaddle, self.playerPaddle
            ], dtype=np.float32)
        else:
            return np.array([
                800 - self.ballPos[0], self.ballPos[1], # pos
                -self.ballVel[0], self.ballVel[1],      # vel
                self.playerPaddle, self.aiPaddle        # paddle
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
        self.ballVel[0] = abs(self.ballVel[0])

        self.ballVel = 2 * self.ballVel / np.sqrt(np.sum(self.ballVel**2)) # normalize the velocity
        self.aiPaddle     = self.size[1] / 2
        self.playerPaddle = self.size[1] / 2
        self.target = None

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, info

    def step(self, action = 0, human = 0):
        if abs(self.ballVel[0]) < 2:
            self.ballVel[0] = np.sign(self.ballVel[0]) * 2

        direction = self._action_to_direction[action]
        reward = 0

        # move ai paddle
        if self.ballVel[0] < 0 or self.render_mode == "human":
            self.aiPaddle += direction
        else:
            self.playerPaddle += direction

        # player input
        if self.render_mode == "human":
            self.playerPaddle = np.clip(self.playerPaddle + human, 50, self.size[1] - 50)
        elif False: # not used when playing against self
            if self.target == None:
                if self.ballVel[0] < 0:
                    self.target = self.size[1] / 2
                else:
                    total_x_distance = self.size[0] - 50 - self.ballPos[0]  # Total x distance until hitting the paddle
                    time = total_x_distance / self.ballVel[0]               # Time to travel this distance
                    total_y_distance = time * self.ballVel[1]               # Total y distance covered (without considering wall bounces)
                    sign = -1 if total_y_distance < 0 else 1
                    total_y_distance = abs(total_y_distance)
                    num_wall_hits = total_y_distance // self.size[1]        # Number of wall hits
                    remaining_distance = total_y_distance % self.size[1]    # Distance covered in the current direction after the last wall hit

                    if num_wall_hits % 2 == 0:
                        # If the number of wall hits is even, the ball is moving in the initial direction
                        self.target = self.ballPos[1] + remaining_distance * sign
                    else:
                        # If it's odd, the ball is moving in the opposite direction
                        self.target = self.size[1] - (self.ballPos[1] + remaining_distance * sign)
            else:
                if self.target > self.playerPaddle:
                    self.playerPaddle += 4
                else:
                    self.playerPaddle -= 4
        
        self.ballPos += self.ballVel

        # clip paddles
        if self.aiPaddle < 0 or self.aiPaddle > self.size[1]:
            self.aiPaddle = np.clip(self.aiPaddle, 50, self.size[1] - 50)
            reward = -0.1
        if self.playerPaddle < 0 or self.playerPaddle > self.size[1]:
            self.playerPaddle = np.clip(self.playerPaddle, 50, self.size[1] - 50)
            reward = -0.1

        # bounce off top and bottom
        if self.ballPos[1] < 10 and self.ballVel[1] < 0 or self.ballPos[1] > self.size[1] - 10 and self.ballVel[1] > 0:
            self.ballVel[1] *= -1

        # bounce off paddles
        ballRect = pg.Rect(self.ballPos[0] - 10, self.ballPos[1] - 10, 20, 20)
        aiPaddleRect = pg.Rect(50, self.aiPaddle - 50, 10, 100)
        playerPaddleRect = pg.Rect(self.size[0] - 50, self.playerPaddle - 50, 10, 100)

        if self.ballVel[0] > 0:
            if ballRect.colliderect(playerPaddleRect):
                self.ballVel[0] *= -1.5
                speed = np.sqrt(np.sum(self.ballVel**2))
                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2))
                differenece = self.ballPos[1] - self.playerPaddle
                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2))
                self.ballVel[1] += differenece / 30

                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2)) * speed

                self.target = None

                reward += 1
        else:
            if ballRect.colliderect(aiPaddleRect):
                self.ballVel[0] *= -1.5
                speed = np.sqrt(np.sum(self.ballVel**2))
                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2))
                differenece = self.ballPos[1] - self.aiPaddle
                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2))
                self.ballVel[1] += differenece / 30

                self.ballVel = self.ballVel / np.sqrt(np.sum(self.ballVel**2)) * speed

                self.target = None

                reward += 1

        terminated = False
        # gain points
        if self.ballPos[0] > self.size[0]:
            self.score[0] += 1
            reward -= (abs(self.playerPaddle - self.ballPos[1])) / 200
            self.reset()
            terminated = True
        elif self.ballPos[0] < 0:
            self.score[1] += 1
            reward -= (abs(self.aiPaddle - self.ballPos[1])) / 200
            self.reset()
            terminated = True

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, reward, terminated, False, info
    
    def render(self):
        if self.render_mode == "rgb_array" or self.render_mode == "human":
            return self._render_frame()

    def _render_frame(self):
        if self.window is None and self.render_mode == "human":
            pg.init()
            pg.display.init()
            self.window = pg.display.set_mode(self.size)
        if self.clock is None and self.render_mode == "human":
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