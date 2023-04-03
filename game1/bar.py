import const

class Bar:
    def __init__(self, x = const.SCREEN_WIDTH / 2, y =const.SCREEN_HEIGHT - 50, width = 100, height = 4):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        pass

    def draw(self):
        stroke('#000000')
        strokeWeight(4)
        line(self.x - self.width / 2, self.y, self.x + self.width / 2, self.y)
