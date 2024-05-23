import time

class Coroutine:
    def __init__(self, func) -> None:
        self._func = func
        self.reset()

    def __call__(self):
        if self.func is None:
            return
        if time.time() > self.lastCall:
            self.lastCall = next(self.func, 0) + time.time()
        else: 
            return

    def reset(self):
        if self._func is not None:
            self.func = self._func()
            self.lastCall = 0
        else:
            self.func = None