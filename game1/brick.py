from object import Block
import const

class Brick(Block):
    def __init__(self, *args, **kwargs):
        super(Brick, self).__init__(*args, **kwargs)
        self.addEventListener('collision', self.__collisionEventHandler)

    def draw(self):
        fill(self.color)
        rect(self.x, self.y, self.width, self.height)

    def __collisionEventHandler(self, collisionEvent):
        self.isDeleted = True

class Wall(Block):
    def __init__(self, *args, **kwargs):
        super(Wall, self).__init__(*args, **kwargs)
        self.color = '#ff0000'

    def draw(self):
        fill(self.color)
        rect(self.x, self.y, self.width, self.height)

def createBrickMap(row = 10, column = 4):
    brick_width = const.SCREEN_WIDTH / row
    brick_height = const.SCREEN_HEIGHT / column / 2
    bricks = []
    for i in range(column):
        for ii in range(row):
            brick = Brick(ii * brick_width, i * brick_height, brick_width, brick_height, '#0f0f0f')
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
            if (rawBrick == 'b'):
                block = Brick(ii * block_width, i * block_height, block_width, block_height, '#0f0f0f')
                blocks.append(block)   
            elif (rawBrick == 'w'):
                block = Wall(ii * block_width, i * block_height, block_width, block_height, '#0f0f0f')
                blocks.append(block)

    return blocks
