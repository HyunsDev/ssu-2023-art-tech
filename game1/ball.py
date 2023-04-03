import const

class Ball:
    def __init__(self, x = const.SCREEN_WIDTH / 2, y = const.SCREEN_HEIGHT / 4 * 3, color = '#000000'):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        fill(self.color)
        strokeWeight(0)
        ellipse(self.x, self.y, const.BALL_SIZE, const.BALL_SIZE)