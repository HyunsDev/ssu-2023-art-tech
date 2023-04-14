import const
from object import Entity
from event import BallCreatedEvent, ItemUsedEvent
from bar import Bar
from ball import Ball


class Item(Entity):
    def __init__(self, x, y, speed=5, width=50, height=50, **kwargs):
        super(Item, self).__init__(x, y, width, height, **kwargs)
        self.speed = speed
        pass

    def draw(self):
        fill("#000000")
        rect(self.x, self.y, self.width, self.height)

    def move(self):
        self.y += self.speed


class AddBallItem(Item):
    def __init__(self, x, y, speed=5, width=50, height=50, **kwargs):
        super(AddBallItem, self).__init__(x, y, speed, width, height, **kwargs)
        self.addEventListener("collision", self._collisionEventHandler)

    def draw(self):
        fill("#000000")
        rect(self.x, self.y, self.width, self.height)

    def _collisionEventHandler(self, event):
        if event.direction == None:
            return
        if isinstance(event.targetObject, (Bar,)):
            if event.direction == "bottom":
                ball = Ball()
                self.game.dispatchEvent(BallCreatedEvent(ball))
                self.game.dispatchEvent(ItemUsedEvent(self))

    # def _collisionEventHandler(self, event):
    #     if event.direction == None:
    #         return
    #     if isinstance(event.targetObject, (Bar,)):
    #         if event.direction == "bottom":
    #             self.game.dispatchEvent()
