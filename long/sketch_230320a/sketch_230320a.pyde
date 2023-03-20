BALL_SPEED = 10
BALL_SIZE = 50

x, y = 100, 100
dirxX = 'right'
dirxY = 'bottom'
control = 'auto'


def setup():
    size(800, 600)
    frameRate(60)
    
def draw():
    # Init
    global x, y, dirxX, dirxY
    background(255)
    
    # Draw
    if x < width / 2:
        if y < height / 2:
            fill('#ff0000')
        else:
            fill("#00ff00")
    else:
        if y < height / 2:
            fill('#0000ff')
        else:
            fill("#ff00ff")
    
    ellipse(x, y, BALL_SIZE, BALL_SIZE)
    
    if control == 'auto':
        # Calc
        x += BALL_SPEED if dirxX == 'right' else -BALL_SPEED
        if x > 800 - BALL_SIZE / 2 and dirxX == 'right': dirxX = 'left'
        if x < 0 + BALL_SIZE / 2 and dirxX == 'left': dirxX = 'right'
        
        y += BALL_SPEED if dirxY == 'bottom' else -BALL_SPEED
        if y > 600 - BALL_SIZE / 2 and dirxY == 'bottom': dirxY = 'top'
        if y < 0 + BALL_SIZE / 2 and dirxY == 'top': dirxY = 'bottom'
    else:
        x = mouseX
        y = mouseY
    
def mouseClicked():
    global control
    control = 'mouse' if control == 'auto' else 'auto'
     
    
    
