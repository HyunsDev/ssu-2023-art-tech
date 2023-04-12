import const
from object import Entity


class Bar(Entity):
    def __init__(
        self,
        x=const.SCREEN_WIDTH / 2,
        y=const.SCREEN_HEIGHT - 50,
        width=150,
        height=10,
        color="#000000",
        **kwargs
    ):
        super(Bar, self).__init__(x, y, width, height, color, **kwargs)
        pass

    def draw(self):
        fill("#000000")
        rect(self.x, self.y, self.width, self.height)

    def move(self):
        # Mouse Event
        self.x = mouseX - self.width / 2
