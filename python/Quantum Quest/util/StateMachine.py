from collections import namedtuple

State = namedtuple('State', 'update coroutine begin end')

class StateMachine:
    def __init__(self, state) -> None:
        self.states = []
        self._state = state

    def addState(self, update, coroutine, begin, end):
        self.states.append(State(update, coroutine, begin, end))

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if value >= len(self.states) or value < 0:
            raise Exception("StateMachine state out of range")

        if self.states[self._state].end != None:
            self.states[self._state].end()
        self._state = value
        if self.states[self._state].begin != None:
            self.states[self._state].begin()

    def update(self):
        if self.states[self._state].update != None:
            self.states[self._state].update()
        if self.states[self._state].coroutine != None:
            next(self.states[self._state].coroutine)