from atom import Atom


class Window(Atom):
    def __init__(
        self,
        title,
        x=0,
        y=0,
        width=200,
        height=300,
    ):
        super(Atom, self).__init__()
        self.title = title
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        # background
        c = color(50, 60, 80, 80)
        fill(c)
        noStroke()
        rect(self.x, self.y, self.width, self.height)

        # title
        text(
            "Hello",
            self.x,
            self.y,
        )
