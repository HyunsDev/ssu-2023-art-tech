

class Brick:
    def __init__(self, x, y, width, height, color = '#f1f1f1'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        fill(self.color)
        rect(self.x, self.y, self.width, self.height)
