from object import Block
from event import BrickDeathEvent, ItemCreatedEvent, BoomEvent, getPointEvent
from item import AddBallItem, BarSizeUpItem
from ball import Ball
import const


class Brick(Block):
    def __init__(self, life=1, *args, **kwargs):
        super(Brick, self).__init__(*args, **kwargs)
        self.life = life

        if self.__class__.__name__ == "Brick":
            self.addEventListener("collision", self._collisionEventHandler)

    def draw(self):
        strokeWeight(0)

        if self.life == 1:
            c = color(214, 214, 214, 100)
            fill(c)
        elif self.life == 2:
            c = color(214, 214, 214, 140)
            fill(c)
        elif self.life == 3:
            c = color(214, 214, 214, 180)
            fill(c)

        stroke(0)
        rect(self.x, self.y, self.width, self.height)

        if const.DEBUG_MODE:
            fill("#ff0000")
            textSize(16)
            textAlign(CENTER, CENTER)
            text(self.life, self.x + self.width / 2, self.y + self.height / 2)

    def _collisionEventHandler(self, event):
        if event.object.canBreakBlock:
            self.life -= 1
            if self.life <= 0:
                self.game.dispatchEvent(BrickDeathEvent(self))
                self.game.dispatchEvent(getPointEvent(10))


class ItemBrick(Brick):
    def __init__(self, item, *args, **kwargs):
        super(ItemBrick, self).__init__(*args, **kwargs)
        self.item = item
        self.life = 1

        if self.__class__.__name__ == "ItemBrick":
            self.addEventListener("collision", self._collisionEventHandler)

    def draw(self):
        strokeWeight(0)
        c = color(54, 180, 90, 80)
        fill(c)

        c = color(54, 180, 90, 255)
        strokeWeight(4)
        stroke(c)

        rect(self.x, self.y, self.width, self.height)

    def _collisionEventHandler(self, event):
        if event.object.canBreakBlock:
            self.life -= 1
            if self.life <= 0:
                self.game.dispatchEvent(ItemCreatedEvent(self.item))
                self.game.dispatchEvent(BrickDeathEvent(self))
                self.game.dispatchEvent(getPointEvent(10))

                self.setTimeout(self.p, 3)

    def p(self):
        print("Hello!!")


class Wall(Block):
    def __init__(self, *args, **kwargs):
        super(Wall, self).__init__(*args, **kwargs)
        self.color = "#ff0000"

    def draw(self):
        strokeWeight(0)
        fill("#ffffff")
        rect(self.x, self.y, self.width, self.height)


class TntBrick(Brick):
    def __init__(self, *args, **kwargs):
        super(TntBrick, self).__init__(*args, **kwargs)
        self.size = 50

        if self.__class__.__name__ == "TntBrick":
            self.addEventListener("collision", self._collisionEventHandler)

    def draw(self):
        strokeWeight(0)
        fill("#ff0000")
        rect(self.x, self.y, self.width, self.height)

        img = loadImage("image/at-tnt.png")
        image(
            img, (self.x + self.width / 2) - 50 / 2, (self.y + self.height / 2) - 50 / 2
        )

    def _collisionEventHandler(self, event):
        if event.object.canBreakBlock:
            self.life -= 1
            if self.life <= 0:
                self.game.dispatchEvent(BrickDeathEvent(self))
                self.game.dispatchEvent(
                    BoomEvent(self.x + self.width / 2, self.y + self.height / 2, 200)
                )
                self.game.dispatchEvent(getPointEvent(10))
