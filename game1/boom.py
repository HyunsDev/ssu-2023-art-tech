from object import Entity


class Boom(Entity):
    def __init__(self, x, y, range, **kwargs):
        super(Boom, self).__init__(x, y, range, range, **kwargs)
        self.range = range
        self.size = 0
        self.direction = "increase"

    def draw(self):
        fill("#ff0000")
        strokeWeight(0)
        circle(self.x, self.y, self.size)

    def getHitbox(self):
        return {
            "x": self.x - self.size / 2,
            "y": self.y - self.size / 2,
            "width": self.size,
            "height": self.size,
        }

    def move(self):
        if self.direction == "increase":
            self.size += 20
            self.width = self.size
            self.height = self.size
        else:
            self.size -= 20
            self.width = self.size
            self.height = self.size

        if self.size >= self.range:
            self.direction = "decrease"

        if self.size <= 0:
            self.game.removeEntity(self)
