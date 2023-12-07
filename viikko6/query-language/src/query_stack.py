
class QueryStack:
    def __init__(self):
        self.stack = []

    def push(self, matcher):
        self.stack.append(matcher)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return len(self.stack) == 0