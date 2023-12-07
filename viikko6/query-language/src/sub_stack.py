
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class PlaysInStack:
    def __init__(self, stack, team):
        self.stack = stack

    def push(self, matcher):
        self.stack.push(matcher)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return len(self.stack) == 0