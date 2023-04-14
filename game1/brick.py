from object import Block
from event import BrickDeathEvent, ItemCreatedEvent
from item import AddBallItem
from ball import Ball
import const


class Brick(Block):
    def __init__(self, life=1, *args, **kwargs):
        super(Brick, self).__init__(*args, **kwargs)
        self.life = life

        if self.__class__.__name__ == "Brick":
            self.addEventListener("collision", self._collisionEventHandler)

    def draw(self):
        if self.life == 1:
            fill("#00ff00")
        elif self.life == 2:
            fill("#ff0000")
        elif self.life == 3:
            fill("#999999")

        stroke(0)
        rect(self.x, self.y, self.width, self.height)

    def _collisionEventHandler(self, event):
        if event.object.__class__.__name__ == "Ball":
            self.life -= 1
            if self.life <= 0:
                self.game.dispatchEvent(BrickDeathEvent(self))


class ItemBrick(Brick):
    def __init__(self, item, *args, **kwargs):
        super(ItemBrick, self).__init__(*args, **kwargs)
        self.item = item

        if self.__class__.__name__ == "ItemBrick":
            self.addEventListener("collision", self._collisionEventHandler)

    def _collisionEventHandler(self, event):
        if event.object.__class__.__name__ == "Ball":
            self.life -= 1
            if self.life <= 0:
                self.game.dispatchEvent(ItemCreatedEvent(self.item))
                self.game.dispatchEvent(BrickDeathEvent(self))


class Wall(Block):
    def __init__(self, *args, **kwargs):
        super(Wall, self).__init__(*args, **kwargs)
        self.color = "#ff0000"

    def draw(self):
        fill("#000000")
        rect(self.x, self.y, self.width, self.height)


def createBrickMap(row=10, column=4):
    brick_width = const.SCREEN_WIDTH / row
    brick_height = const.SCREEN_HEIGHT / column / 2
    bricks = []
    for i in range(column):
        for ii in range(row):
            brick = Brick(
                ii * brick_width, i * brick_height, brick_width, brick_height, "#0f0f0f"
            )
            bricks.append(brick)
    return bricks


# Map Example
# mapData = [
#     ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
#     ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
#     ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
#     ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
#     ['w', 'w', 'w', 'w', 'b', 'b', 'w', 'w', 'w', 'w'],
# ]


def createBlockMapByMap(map):
    block_width = const.SCREEN_WIDTH / len(map[0])
    block_height = const.SCREEN_HEIGHT / len(map) / 2
    blocks = []
    for i, mapRow in enumerate(map):
        for ii, rawBrick in enumerate(mapRow):
            if rawBrick == "b":  # Brick
                block = Brick(
                    x=ii * block_width,
                    y=i * block_height,
                    width=block_width,
                    height=block_height,
                )
                blocks.append(block)

            elif rawBrick == "w":  # Wall
                block = Wall(
                    x=ii * block_width,
                    y=i * block_height,
                    width=block_width,
                    height=block_height,
                )
                blocks.append(block)

            elif rawBrick == "1":  # Brick (life: 1)
                block = Brick(
                    x=ii * block_width,
                    y=i * block_height,
                    width=block_width,
                    height=block_height,
                    life=1,
                )
                blocks.append(block)

            elif rawBrick == "2":  # Brick (life: 2)
                block = Brick(
                    x=ii * block_width,
                    y=i * block_height,
                    width=block_width,
                    height=block_height,
                    life=2,
                )
                blocks.append(block)

            elif rawBrick == "3":  # Brick (life: 3)
                block = Brick(
                    x=ii * block_width,
                    y=i * block_height,
                    width=block_width,
                    height=block_height,
                    life=3,
                )
                blocks.append(block)

            elif rawBrick == " ":  # Empty
                pass

            elif rawBrick == "a":  # ItemBrick (item: addBall)
                item = AddBallItem(x=ii * block_width, y=i * block_height)
                block = ItemBrick(
                    x=ii * block_width,
                    y=i * block_height,
                    width=block_width,
                    height=block_height,
                    item=item,
                )
                blocks.append(block)

    return blocks
