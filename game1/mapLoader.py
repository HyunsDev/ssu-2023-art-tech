from object import Block
from event import BrickDeathEvent, ItemCreatedEvent
from item import AddBallItem, BarSizeUpItem
from ball import Ball
from brick import Brick, ItemBrick, Wall, TntBrick
import const


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

            elif rawBrick == "t":  # Brick (life: 3)
                block = TntBrick(
                    x=ii * block_width,
                    y=i * block_height,
                    width=block_width,
                    height=block_height,
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

            elif rawBrick == "s":  # ItemBrick (item: addBall)
                item = BarSizeUpItem(x=ii * block_width, y=i * block_height)
                block = ItemBrick(
                    x=ii * block_width,
                    y=i * block_height,
                    width=block_width,
                    height=block_height,
                    item=item,
                )
                blocks.append(block)

    return blocks
