# snake gymnasium env
import gymnasium as gym
import numpy as np
import pygame as pg

dirToVec = {
    1: np.array((0, -1), dtype=np.int8),
    2: np.array((1, 0), dtype=np.int8),
    3: np.array((0, 1), dtype=np.int8),
    4: np.array((-1, 0), dtype=np.int8)
}

class SnakeEnv(gym.Env):
    def __init__(self, size = 20, grid_size = 30, render_mode="rgb_array") -> None:
        self.metadata = {
            "render_modes": ["human", "rgb_array"],
            "render_fps": 4,
        }
        self.grid_size = grid_size
        
        self.size = size
        self.reset()
        self.action_space = gym.spaces.Discrete(4)
        self.observation_space = gym.spaces.Box(low=0, high=4, shape=(2, size, size), dtype=np.int8)

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        self.window = None
        self.clock = None

    #def _get_obs(self):
    #    obs = np.zeros((2, self.size, self.size), dtype=np.int8)
    #    obs[0] = self.snake
    #    obs[1][self.head[0]][self.head[1]]   = 1
    #    obs[1][self.tail[0]][self.tail[1]]   = 2
    #    obs[1][self.apple[0]][self.apple[1]] = 3
    #    return obs
    
    
    def _get_info(self):
        return {
            "length": self.length
        }
    
    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        self.length = 3
        self.head   = np.array((self.size // 2   , self.size // 2), dtype=np.int8)
        self.tail   = np.array((self.size // 2 -2, self.size // 2), dtype=np.int8)
        self.apple  = np.array((self.size // 2 +5, self.size // 2), dtype=np.int8)
        self.dir    = 2
        self.steps  = 0

        self.snake = np.zeros(shape=(self.size, self.size))
        self.snake[self.tail[0]: self.head[0]][:,self.head[1]] = self.dir
        self.step(1)

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, info
    
    def step(self, action):
        reward = 0
        self.steps += 1
        terminated = False

        self.dir = action+1
        self.snake[self.head[0]][[self.head[1]]] = self.dir
        self.head += dirToVec[self.dir]

        # apple
        if np.all(self.head == self.apple):
            self.steps = 0
            reward += 1
            self.length += 1
            posible = np.array(np.nonzero(self.snake == 0))
            self.apple = posible[:,np.random.randint(0, posible.shape[1]-1)]
        else:
            temp = self.tail.copy()
            self.tail += dirToVec[self.snake[self.tail[0]][self.tail[1]]]
            self.snake[temp[0]][temp[1]] = 0

        # if moving in direction of apple
        idx = np.nonzero(self.dir)[0][0]
        diff = self.apple[idx] - self.head[idx]
        reward += 0.1 if np.sign(diff) == np.sign(dirToVec[self.dir][idx]) or diff == 0 else -0.1

        # collision
        if self.steps > 200 or self.head[0] < 0 or self.head[0] >= self.size or self.head[1] < 0 or self.head[1] >= self.size or self.snake[self.head[0]][self.head[1]] != 0:
            reward += -1
            terminated = True
            self.reset()
        else:
            self.snake[self.head[0]][[self.head[1]]] = self.dir

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
            self.window = pg.display.set_mode((self.size*self.grid_size, self.size*self.grid_size))
        if self.clock is None and self.render_mode == "human":
            self.clock = pg.time.Clock()

        pg.font.init()
        canvas = pg.Surface((self.size*self.grid_size, self.size*self.grid_size))

        canvas.fill((0,0,0))
        for j in range(self.size):
            for i in range(self.size):
                if self.snake[i][j] != 0:
                    pg.draw.rect(canvas, (0,255,0), (i * self.grid_size, j * self.grid_size, self.grid_size, self.grid_size))
                elif self.apple[0] == i and self.apple[1] == j:
                    pg.draw.rect(canvas, (255,0,0), (i * self.grid_size, j * self.grid_size, self.grid_size, self.grid_size))

        for i in range(1,self.size): # grid
            pg.draw.line(canvas, (255,255,255), (i*self.grid_size, 0), (i*self.grid_size, self.size*self.grid_size))
            pg.draw.line(canvas, (255,255,255), (0, i*self.grid_size), (self.size*self.grid_size, i*self.grid_size))
        
        font = pg.font.SysFont('didot.ttc', 50) # len
        img = font.render(str(self.length), True, (255,255,255))
        canvas.blit(img, (self.size*self.grid_size - img.get_width() - 10, 10))

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