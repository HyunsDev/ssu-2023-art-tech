class Event:
    def __init__(self, object):
        self.type = "event"
        pass


class CollisionEvent(Event):
    def __init__(self, object, targetObject, direction, reverseDirection):
        self.type = "collision"
        self.object = object
        self.targetObject = targetObject
        self.direction = direction
        self.reverseDirection = reverseDirection


class BallDeathEvent(Event):
    def __init__(self, ball):
        self.type = "ballDeath"
        self.object = ball


class BallCreatedEvent(Event):
    def __init__(self, ball):
        self.type = "ballCreated"
        self.ball = ball


class BarSizeUpEvent(Event):
    def __init__(self, bar):
        self.type = "barSizeUp"


class BoomEvent(Event):
    def __init__(self, x, y, size):
        self.type = "boom"
        self.x = x
        self.y = y
        self.size = size


class BrickDeathEvent(Event):
    def __init__(self, brick):
        self.type = "brickDeath"
        self.object = brick


class ItemUsedEvent(Event):
    def __init__(self, item):
        self.type = "itemUsed"
        self.item = item


class GameOverEvent(Event):
    def __init__(self):
        self.type = "gameOver"


class StageClearEvent(Event):
    def __init__(self):
        self.type = "stageClear"


class MouseClickEvent(Event):
    def __init__(self, x, y):
        self.type = "mouseClick"
        self.x = x
        self.y = y


class ItemCreatedEvent(Event):
    def __init__(self, item):
        self.type = "itemCreated"
        self.item = item
