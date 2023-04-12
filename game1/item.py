import const
from object import Entity
from event import BallCreatedEvent
from bar import Bar


class Item(Entity):
    def __init__(self, x, y, speed=5, width=50, height=50, color="#000000", **kwargs):
        super(Item, self).__init__(x, y, width, height, color, **kwargs)
        self.speed = speed
        pass

    def draw(self):
        fill("#000000")
        rect(self.x, self.y, self.width, self.height, self.width)

    def move(self):
        self.y += self.speed


class AddBallItem(Item):
    def __init__(self, x, y, speed=5, width=50, height=50, color="#000000", **kwargs):
        super(AddBallItem, self).__init__(x, y, speed, width, height, color, **kwargs)
        pass

    def draw(self):
        fill("#000000")
        rect(self.x, self.y, self.width, self.height, self.width)

    # def _collisionEventHandler(self, event):
    #     if event.direction == None:
    #         return
    #     if isinstance(event.targetObject, (Bar,)):
    #         if event.direction == "bottom":
    #             self.game.dispatchEvent()
