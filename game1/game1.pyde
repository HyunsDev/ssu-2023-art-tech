import const
from game import Game

game = Game()

def setup():
    size(const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
    game.init()


def draw():
    game.draw()

def mousePressed():
    game.mousePressEvent(mouseX, mouseY)