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
    def __init__(self):
        self.type = "ballCreated"


class BarSizeUpEvent(Event):
    def __init__(self):
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


class KeyboardPressEvent(Event):
    def __init__(self, key):
        self.type = "keyboardPress"
        self.key = key


class ItemCreatedEvent(Event):
    def __init__(self, item):
        self.type = "itemCreated"
        self.item = item


class getPointEvent(Event):
    def __init__(self, point):
        self.type = "getPoint"
        self.point = point


class godModeEvent(Event):
    def __init__(self):
        self.type = "godMode"


class ShotBallStartEvent(Event):
    def __init__(self):
        self.type = "shotBallStart"


class ShotBallEvent(Event):
    def __init__(self, x, y):
        self.type = "shotBall"
        self.x = x
        self.y = y
