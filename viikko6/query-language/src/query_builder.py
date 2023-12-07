
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from sub_stack import PlaysInStack
from query_stack import QueryStack

class QueryBuilder:
    def __init__(self, stack = QueryStack()):
        self.stack = stack

    def build(self):
        return All()

    def playsIn(self, team):
        return QueryBuilder(PlaysInStack(self.stack,team))

    def hasAtLeast(self, value, attr):
        return HasAtLeast(value, attr)

    def hasFewerThan(self, value, attr):
        return HasFewerThan(value, attr)

    def or_(self, *matchers):
        return Or(*matchers)

    def not_(self, matcher):
        return Not(matcher)

    def and_(self, *matchers):
        return And(*matchers)