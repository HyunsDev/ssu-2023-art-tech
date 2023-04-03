import const
from brick import Brick

class Map:
    _map = []

    def __init__(self):
        pass

    # Create Bricks 
    def autoGenerate(self, row = 10, column = 4):
        brick_width = const.SCREEN_WIDTH / row
        brick_height = const.SCREEN_HEIGHT / column / 2
        bricks = []
        for i in range(column):
            for ii in range(row):
                brick = Brick(ii * brick_width, i * brick_height, brick_width, brick_height)
                bricks.append(brick)
                
        self._map = bricks
    

    # Draw Object In Map Data
    def draw(self):
        self.__drawBricks()

    
    def __drawBricks(self):
        for brick in self._map:
            brick.draw()
