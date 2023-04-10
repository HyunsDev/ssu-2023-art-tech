# Event Types: collision
class Event:
    def __init__(self, object):
        self.type = 'event'
        pass

class CollisionEvent(Event):
    def __init__(self, object, targetObject, direction, reverseDirection):
        self.type = 'collision'
        self.object = object
        self.targetObject = targetObject
        self.direction = direction
        self.reverseDirection = reverseDirection

class BallDeathEvent(Event):
    def __init__(self, ball):
        self.type = 'ballDeath'
        self.object = ball

class GameOverEvent(Event):
    def __init__(self):
        self.type = 'gameOver'

class MouseClickEvent(Event):
    def __init__(self, x, y):
        self.type = 'mouseClick'
        self.x = x
        self.y = y

class ItemCreateEvent(Event):
    def __init__(self, item):
        self.type = 'itemCreate'
        self.item = item