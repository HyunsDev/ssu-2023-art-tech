import const
from object import Entity, Object, Block
from bar import Bar
import math
from event import BallDeathEvent


def getAngle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    angle = math.atan2(dy, dx)
    return math.degrees(angle)


class Ball(Entity):
    def __init__(
        self,
        x=const.SCREEN_WIDTH / 2,
        y=const.SCREEN_HEIGHT / 4 * 3,
        ball_size=const.BALL_SIZE,
        ball_speed=8.0,
        **kwargs
    ):
        super(Ball, self).__init__(x, y, ball_size, ball_size, **kwargs)
        self.x = x
        self.y = y
        self.axis_speed = (ball_speed**2 / 2.0) ** (1 / 2.0)
        self.ax = self.axis_speed
        self.ay = -self.axis_speed
        self.ball_speed = ball_speed
        self.size = ball_size
        self.width = self.size
        self.height = self.size

        self.isGotMode = False
        self.gotModeTimer = None

        self.trajectories = []

        self.addEventListener(
            "collision", lambda event: self.__collisionEventHandler(event)
        )
        self.game.addEventListener("godMode", self.__godModeEventHandler)
        self.game.addEventListener("shotBall", self.__shotBallEventHandler)

    def draw(self):
        # Draw Trajectory
        # c = color()

        if not self.game.isShotMode:
            strokeWeight(self.width)
            beforeTrajectory = (self.x, self.y)
            for i, trajectory in enumerate(self.trajectories):
                c = None
                if self.isGotMode:
                    c = color(255, 255, 0, 255 / (i + 1))
                else:
                    c = color(58, 121, 196, 255 / (i + 1))

                stroke(c)

                line(
                    trajectory[0] + self.size / 2,
                    trajectory[1] + self.size / 2,
                    beforeTrajectory[0] + self.size / 2,
                    beforeTrajectory[1] + self.size / 2,
                )
                beforeTrajectory = trajectory

        # Draw Ball
        if self.isGotMode:
            fill("#ffff00")
            stroke("#ffff00")
        else:
            fill("#10223E")
            stroke("#3A79C4")
        strokeWeight(1)
        ellipse(
            self.x + self.width / 2, self.y + self.height / 2, self.width, self.height
        )

        if self.game.isShotMode:
            strokeWeight(4)
            c = color(58, 121, 196, 80)
            stroke(c)
            line(self.x + self.width / 2, self.y + self.height / 2, mouseX, mouseY)

    def move(self):
        self.x += self.ax
        self.y += self.ay

        self.trajectories.insert(0, (self.x, self.y))
        if len(self.trajectories) > 30:
            self.trajectories.pop()

        if self.x > const.SCREEN_WIDTH - self.size / 2 and self.ax > 0:
            self.ax = abs(self.ax) * -1
        if self.x < 0 + self.size / 2 and self.ax < 0:
            self.ax = abs(self.ax) * 1
        if self.y < 0 + self.size / 2 and self.ay < 0:
            self.ay = abs(self.ay) * 1

        if self.y > const.SCREEN_HEIGHT - self.size / 2 and self.ay > 0:
            self.game.dispatchEvent(BallDeathEvent(self))
            self.ay = abs(self.ay) * -1

    def __collisionEventHandler(self, event):
        if event.direction == None:
            return
        if isinstance(event.targetObject, (Block,)) and not self.isGotMode:
            if event.direction == "left":
                self.ax = abs(self.ax) * -1
            if event.direction == "right":
                self.ax = abs(self.ax) * 1
            if event.direction == "top":
                self.ay = abs(self.ay) * -1
            if event.direction == "bottom":
                self.ay = abs(self.ay) * 1

        elif isinstance(event.targetObject, Bar):
            # distance: -1 ~ 0 ~ 1 (left ~ center ~ right)
            distance = (
                (event.targetObject.x - self.width / 2.0)
                + (event.targetObject.width + self.width) / 2.0
                - self.x
            ) / float((event.targetObject.width + self.width) / 2.0)
            direction = -1 if distance > 0 else 1
            degree = abs(distance) * (90 - 10)

            if event.direction != "bottom":
                self.ax = self.ball_speed * math.sin(math.radians(degree)) * direction
                self.ay = abs(self.ball_speed * math.cos(math.radians(degree))) * -1

    def __godModeEventHandler(self, event):
        def endGotMode():
            self.isGotMode = False
            self.gotModeTimer = None

        self.isGotMode = True
        if self.gotModeTimer:
            self.clearTimeout(self.gotModeTimer)

        self.gotModeTimer = self.setTimeout(endGotMode, 5)

    def __shotBallEventHandler(self, event):
        degree = getAngle(self.x, self.y, event.x, event.y)
        self.ax = self.ball_speed * math.cos(math.radians(degree))
        self.ay = self.ball_speed * math.sin(math.radians(degree))
        self.trajectories = []
