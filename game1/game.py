import const
from bar import Bar
from ball import Ball
from brick import Brick
from object import Object
from atom import Atom
from event import GameOverEvent, MouseClickEvent, KeyboardPressEvent
from window import Window
from mapLoader import createBlockMapByMap
from gameTimer import GameTimer
from boom import Boom


blockMap = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["1", "2", "t", "3", "3", " ", " ", "3", "3", "t", "1", "1"],
    ["1", "1", " ", "3", "3", " ", " ", "3", "3", " ", "1", "1"],
    ["t", "1", " ", " ", " ", "3", "3", " ", " ", " ", "1", "t"],
    ["1", "1", " ", " ", "s", "2", "2", "s", " ", " ", "1", "1"],
    ["g", "w", "t", " ", "a", " ", " ", "a", " ", "t", "w", "g"],
]


class Game(Atom):
    def __init__(self):
        super(Game, self).__init__(self)
        self.game = self

        self.point = 0
        self.isGameOver = False
        self.isShowGameOverScreen = False

        self.gameTimer = GameTimer()

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
        self.addEventListener("getPoint", self.__getPointEventHandler)
        self.addEventListener("boom", self.__boomEventHandler)
        self.addEventListener("keyboardPress", self.__keyboardPressEventHandler)
        self.addEventListener("collision", self.__collisionEventHandler)
        self.addEventListener("mouseClick", self.__mouseClickEventHandler)

    # Initialize Game
    # Execute In setup() Function and Reset Game
    def init(self):
        frameRate(const.FRAME_RATE)
        self.point = 0
        self.isGameOver = False
        self.isShowGameOverScreen = False
        self.blocks = createBlockMapByMap(blockMap)
        self.entities = []
        self.balls = [Ball(const.SCREEN_WIDTH / 3)]
        self.bar = Bar()
        self.window = []

        # debugWindow = Window("title")
        # self.window = [debugWindow]

    # Move & Calc & Draw Object
    # Execute In draw() Function
    def draw(self):
        self.gameTimer.tick()
        self.__move()
        self.__calc()
        self.__drawFrame()

        if const.DEBUG_MODE:
            self.__DEBUG_drawHitbox()
            self.__DEBUG_frameRate()

    # Draw Object, Entity, Window
    def __drawFrame(self):
        background("#030510")

        fill(color(255, 255, 255, 30))
        textSize(100)
        textAlign(CENTER, CENTER)

        if self.isGameOver:
            text("GAME OVER", width / 2, height / 2)

            textSize(30)
            text("Score: %s" % (self.point), width / 2, (height / 2) + 70)

        else:
            text(self.point, width / 2, height / 2)

        map(lambda brick: brick.draw(), self.blocks)
        map(lambda ball: ball.draw(), self.balls)
        map(lambda entity: entity.draw(), self.entities)
        map(lambda window: window.draw(), self.window)
        self.bar.draw()

        if self.isShowGameOverScreen:
            self.__gameOverScreen()

    def __gameOverScreen(self):
        background("#030510")

        fill(color(255, 255, 255, 255))
        textSize(100)
        textAlign(CENTER, CENTER)
        text("One More?", width / 2, (height / 2) - 30)

        textSize(30)
        text("Press any key to restart", width / 2, (height / 2) + 40)

    def __DEBUG_drawHitbox(self):
        map(lambda brick: brick.drawHitbox(), self.blocks)
        map(lambda ball: ball.drawHitbox(), self.balls)
        map(lambda entity: entity.drawHitbox(), self.entities)
        self.bar.drawHitbox()

    def __DEBUG_frameRate(self):
        fill("#ff0000")
        textAlign(LEFT, TOP)
        textSize(16)
        text(frameRate, 0, 0)

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

    #
    def removeEntity(self, entity):
        self.entities.remove(entity)

    #### [ Event Handler ] ####
    def __ballDeathEventHandler(self, event):
        self.balls.remove(event.object)
        if len(self.balls) == 0:
            self.game.dispatchEvent(GameOverEvent())

    def __gameOverEventHandlerCB(self):
        self.isShowGameOverScreen = True

    def __gameOverEventHandler(self, event):
        self.isGameOver = True
        print("Game Over")

        self.setTimeout(self.__gameOverEventHandlerCB, 3)

    def __collisionEventHandler(self, event):
        pass
        # sound = SoundFile(this, "path/to/your/soundfile.mp3")
        # sound.play()

    def __brickDeathEventHandler(self, event):
        self.blocks.remove(event.object)

    def __itemCreatedEventHandler(self, event):
        self.entities.append(event.item)

    def __ballCreatedEventHandler(self, event):
        self.balls.append(event.ball)

    def __itemUsedEventHandler(self, event):
        self.entities.remove(event.item)

    def __getPointEventHandler(self, event):
        self.point += event.point

    def __boomEventHandler(self, event):
        boom = Boom(event.x, event.y, event.size)
        self.entities.append(boom)

    def __keyboardPressEventHandler(self, event):
        if event.key == " ":
            const.DEBUG_MODE = not const.DEBUG_MODE

        if self.isShowGameOverScreen:
            self.init()

    def __mouseClickEventHandler(self, event):
        if self.isShowGameOverScreen:
            self.init()

    # Outer Event
    def mousePressEvent(self, x, y):
        self.game.dispatchEvent(MouseClickEvent(x, y))

    def keyboardPressEvent(self, key):
        self.game.dispatchEvent(KeyboardPressEvent(key))
