import const
from bar import Bar
from ball import Ball
from brick import Brick
from object import Object
from atom import Atom
from event import GameOverEvent, MouseClickEvent
from window import Window
from mapLoader import createBlockMapByMap

blockMap = [
    ["1", "t", "1", "1", " ", " ", "1", "1", "t", "1"],
    ["1", " ", "1", "1", " ", " ", "1", "1", " ", "1"],
    ["1", " ", " ", " ", "3", "3", " ", " ", " ", "1"],
    ["1", " ", " ", "s", "2", "2", "s", " ", " ", "1"],
    ["w", "t", " ", "a", " ", " ", "a", " ", "t", "w"],
]


class Game(Atom):
    def __init__(self):
        super(Game, self).__init__(self)
        self.game = self

        self.blocks = []
        self.entities = []
        self.balls = [Ball(const.SCREEN_WIDTH / 3)]
        self.bar = Bar()
        self.window = []

        self.addEventListener("ballDeath", self.__ballDeathEventHandler)
        self.addEventListener("gameOver", self.__gameOverEventHandler)
        self.addEventListener("brickDeath", self.__brickDeathEventHandler)
        self.addEventListener("itemCreated", self.__itemCreatedEventHandler)
        self.addEventListener("ballCreated", self.__ballCreatedEventHandler)
        self.addEventListener("itemUsed", self.__itemUsedEventHandler)

    # Initialize Game
    # Execute In setup() Function
    def init(self):
        frameRate(60)
        self.blocks = createBlockMapByMap(blockMap)

        # debugWindow = Window("title")
        # self.window = [debugWindow]

    # Move & Calc & Draw Object
    # Execute In draw() Function
    def draw(self):
        self.__move()
        self.__calc()
        self.__drawFrame()

        self.__DEBUG_drawHitbox()

    # Draw Object, Entity
    def __drawFrame(self):
        background("#030510")
        map(lambda brick: brick.draw(), self.blocks)
        map(lambda ball: ball.draw(), self.balls)
        map(lambda entity: entity.draw(), self.entities)
        map(lambda window: window.draw(), self.window)
        self.bar.draw()

    def __DEBUG_drawHitbox(self):
        map(lambda brick: brick.drawHitbox(), self.blocks)
        map(lambda ball: ball.drawHitbox(), self.balls)
        map(lambda entity: entity.drawHitbox(), self.entities)
        self.bar.drawHitbox()

    # Move Object
    def __move(self):
        # self.balls.move()
        map(lambda ball: ball.move(), self.balls)
        map(lambda entity: entity.move(), self.entities)
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

    #### [ Event Handler ] ####
    def __ballDeathEventHandler(self, event):
        self.balls.remove(event.object)
        if len(self.balls) == 0:
            self.game.dispatchEvent(GameOverEvent())

    def __gameOverEventHandler(self, event):
        print("Game Over")

    def __brickDeathEventHandler(self, event):
        self.blocks.remove(event.object)

    def __itemCreatedEventHandler(self, event):
        self.entities.append(event.item)

    def __ballCreatedEventHandler(self, event):
        self.balls.append(event.ball)

    def __itemUsedEventHandler(self, event):
        self.entities.remove(event.item)

    # Outer Event
    def mousePressEvent(self, x, y):
        self.game.dispatchEvent(MouseClickEvent(x, y))
