BALL_SPEED = 5
BALL_SIZE = 40
BAR_SIZE = 200

x, y = 100, 100
ball_color = '#000000'
dirxX = 'right'
dirxY = 'bottom'

barX = 0

def setup():
    size(800, 600)
    frameRate(60)
    
def draw():    
    # Init
    global x, y, dirxX, dirxY
    background(255)
    
    # Draw
    drawBall()
    drawBar()
    
    # Calc
    x += BALL_SPEED if dirxX == 'right' else -BALL_SPEED
    if x > 800 - BALL_SIZE / 2 and dirxX == 'right': dirxX = 'left'
    if x < 0 + BALL_SIZE / 2 and dirxX == 'left': dirxX = 'right'
    
    y += BALL_SPEED if dirxY == 'bottom' else -BALL_SPEED
    if y < 0 + BALL_SIZE / 2 and dirxY == 'top': dirxY = 'bottom'
    if y > 600 - BALL_SIZE / 2 and dirxY == 'bottom':
        print('GAME OVER')
        
    # detact Bar
    _bar_left = mouseX - BAR_SIZE / 2
    _bar_right = mouseX + BAR_SIZE / 2
    _bar_height = height - 50
    if y + BALL_SIZE / 2 > _bar_height and x > _bar_left and x < _bar_right:
        dirxY = 'top'
        
    
def mouseClicked():
    global dirxX, dirxY
    # dirxX = 'right' if dirxX == 'left' else 'left'
    dirxY = 'top' if dirxX == 'bottom' else 'bottom'
     
    BALL_SPEED = 10
    BALL_SIZE = 50
    
    x, y = 100, 100
    dirxX = 'right'
    dirxY = 'bottom'

    
def drawBar():
    stroke('#000000')
    strokeWeight(4)
    line(mouseX - BAR_SIZE / 2, height - 50, mouseX + BAR_SIZE / 2, height - 50)
    
def drawBall():
    fill(ball_color)
    strokeWeight(0)
    ellipse(x, y, BALL_SIZE, BALL_SIZE)
    
