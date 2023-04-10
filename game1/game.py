import const
from bar import Bar 
from ball import Ball
from brick import createBrickMap, createBlockMapByMap, Brick
from object import Object
from atom import Atom
from event import GameOverEvent, MouseClickEvent

blockMap = [
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['w', 'w', 'w', 'w', 'b', 'b', 'w', 'w', 'w', 'w'],
]
class Game(Atom):
    def __init__(self):
        super(Game, self).__init__(self)
        self.game = self

        self.blocks = []
        self.entities = []
        self.balls = [ Ball(const.SCREEN_WIDTH / 3) ]
        self.bar = Bar()

        self.addEventListener('ballDeath', self.__ballDeathEventHandler)
        self.addEventListener('gameOver', self.__gameOverEventHandler)
        self.addEventListener('mouseClick', self.__mousePressEventHandler)

    # Initialize Game
    # Execute In setup() Function
    def init(self):
        frameRate(60)
        self.blocks = createBlockMapByMap(blockMap)

    # Move & Calc & Draw Object
    # Execute In draw() Function
    def draw(self):
        self.__move()
        self.__calc()
        self.__drawFrame()
        self.__removeDeletedObject()

    # Draw Object, Entity
    def __drawFrame(self):
        background(255)
        map(lambda brick: brick.draw(), self.blocks)
        map(lambda ball: ball.draw(), self.balls)
        self.bar.draw()

    # Move Object
    def __move(self):
        # self.balls.move()
        map(lambda ball: ball.move(), self.balls)
        self.bar.move()

    # Collision Detection
    def __calc(self):
        for ball in self.balls:
            for block in self.blocks:
                # Ball - Block Collision
                Object.collision(self.game, ball, block)
            # Ball - Bar Collision
            Object.collision(self.game, ball, self.bar)

        for entity in self.entities:
            for block in self.blocks:
                # Entity - Block Collision
                Object.collision(self.game, entity, block)
            # Entity - Bar Collision
            Object.collision(self.game, entity, self.bar)

    def __removeDeletedObject(self):
        self.blocks = filter(lambda brick: not brick.isDeleted, self.blocks)
        self.balls = filter(lambda ball: not ball.isDeleted, self.balls)

    # Event Handler
    def __ballDeathEventHandler(self, event):
        self.balls.remove(event.object)
        if len(self.balls) == 0:
            self.game.dispatchEvent(GameOverEvent())

    def __gameOverEventHandler(self, event):
        print('Game Over')
    
    def __mousePressEventHandler(self, event):
        print(event.x, event.y, event.type)
        self.blocks.append(Brick(event.x, event.y, 50, 50, '#000000'))

    # Outer Event
    def mousePressEvent(self, x, y):
        self.game.dispatchEvent(MouseClickEvent(x, y))