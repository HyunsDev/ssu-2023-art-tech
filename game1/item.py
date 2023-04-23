import const
from object import Entity
from event import (
    BallCreatedEvent,
    ItemUsedEvent,
    BarSizeUpEvent,
    godModeEvent,
    ShotBallStartEvent,
)
from bar import Bar
from ball import Ball


class Item(Entity):
    def __init__(self, x, y, speed=5, width=50, height=50, **kwargs):
        super(Item, self).__init__(x, y, width, height, **kwargs)
        self.speed = speed
        self.canBreakBlock = False
        self.image = None
        pass

    def draw(self):
        img = loadImage(self.image)
        image(img, self.x, self.y)

    def move(self):
        self.y += self.speed


class AddBallItem(Item):
    def __init__(self, x, y, speed=5, width=50, height=50, **kwargs):
        super(AddBallItem, self).__init__(x, y, speed, width, height, **kwargs)
        self.addEventListener("collision", self._collisionEventHandler)
        self.image = "image/at-addBallItem.png"

    def _collisionEventHandler(self, event):
        if event.direction == None:
            return
        if isinstance(event.targetObject, (Bar,)):
            self.game.dispatchEvent(BallCreatedEvent())
            self.game.dispatchEvent(ItemUsedEvent(self))


class BarSizeUpItem(Item):
    def __init__(self, x, y, speed=5, width=50, height=50, **kwargs):
        super(BarSizeUpItem, self).__init__(x, y, speed, width, height, **kwargs)
        self.addEventListener("collision", self._collisionEventHandler)
        self.image = "image/at-barSizeUpItem.png"

    def _collisionEventHandler(self, event):
        if event.direction == None:
            return
        if isinstance(event.targetObject, (Bar,)):
            self.game.dispatchEvent(BarSizeUpEvent())
            self.game.dispatchEvent(ItemUsedEvent(self))


class GodBallItem(Item):
    def __init__(self, x, y, speed=5, width=50, height=50, **kwargs):
        super(GodBallItem, self).__init__(x, y, speed, width, height, **kwargs)
        self.addEventListener("collision", self._collisionEventHandler)
        self.image = "image/at-godBallItem.png"

    def _collisionEventHandler(self, event):
        if event.direction == None:
            return
        if isinstance(event.targetObject, (Bar,)):
            self.game.dispatchEvent(godModeEvent())
            self.game.dispatchEvent(ItemUsedEvent(self))


class ShotBallItem(Item):
    def __init__(self, x, y, speed=5, width=50, height=50, **kwargs):
        super(ShotBallItem, self).__init__(x, y, speed, width, height, **kwargs)
        self.addEventListener("collision", self._collisionEventHandler)
        self.image = "image/at-shotBallItem.png"

    def _collisionEventHandler(self, event):
        if event.direction == None:
            return
        if isinstance(event.targetObject, (Bar,)):
            self.game.dispatchEvent(ItemUsedEvent(self))
            self.game.dispatchEvent(ShotBallStartEvent())
