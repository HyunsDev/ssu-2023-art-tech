import const
from map import Map
from bar import Bar 
from ball import Ball

class Game:
    def __init__(self):
        self.map = Map()
        self.ball = Ball()
        self.bar = Bar()

        pass

    def init(self):
        frameRate(60)
        self.map.autoGenerate()

    def drawFrame(self):
        background(255)
        self.map.draw()
        self.ball.draw()
        self.bar.draw()
