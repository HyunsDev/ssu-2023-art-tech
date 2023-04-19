import const
from object import Entity, Object, Block
from bar import Bar
import math
from event import BallDeathEvent


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

        self.trajectories = []

        self.addEventListener(
            "collision", lambda event: self.__collisionEventHandler(event)
        )

    def draw(self):
        # Draw Trajectory
        # c = color()
        strokeWeight(self.width)
        beforeTrajectory = (self.x, self.y)
        for i, trajectory in enumerate(self.trajectories):
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
        fill("#10223E")
        stroke("#3A79C4")
        strokeWeight(1)
        ellipse(
            self.x + self.width / 2, self.y + self.height / 2, self.width, self.height
        )

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
        if isinstance(event.targetObject, (Block,)):
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
