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
        self.game.addEventListener("barSizeUp", self._barSizeUpEventHandler)
        pass

    def draw(self):
        fill("#3A79C4")
        strokeWeight(0)
        rect(self.x, self.y, self.width, 5)

    def move(self):
        # Mouse Event
        self.x = mouseX - self.width / 2

    def _barSizeUpEventHandler(self, event):
        self.width += 50
