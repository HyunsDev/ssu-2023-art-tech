BALL_SPEED = 5
BALL_SIZE = 40
BAR_SIZE = 200

BRICKS_ROW = 10
BRICKS_COLUMN = 4  

x, y = 400, 350
ball_color = '#000000'
dirxX = 'right'
dirxY = 'bottom'
bricks = []
# brick = [x1, y1, x2, y2]

brick_size = 100, 100

barX = 0

def setup():
    global bricks
    
    size(800, 600)
    frameRate(60)
    
    # fill bricks
    brick_size = width / BRICKS_ROW, height / (BRICKS_COLUMN * 2)
    nowBricks = []
    for i in range(BRICKS_COLUMN):
        for ii in range(BRICKS_ROW):
            brick = [ ii * brick_size[0], i * brick_size[1], (ii + 1) * brick_size[0], (i + 1) * brick_size[1]]
            print(brick)
            bricks.append(brick)
            
    print(bricks)
        
    
    
def draw():    
    # Init
    global x, y, dirxX, dirxY
    background(255)
    
    # Draw
    drawBricks()
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
        
    # collision detection
    i = 0
    for brick in bricks:
        if (brick[0] <= x + BALL_SIZE / 2 and brick[2] >= x - BALL_SIZE / 2
            and brick[1] <= y + BALL_SIZE / 2 and brick[3] >= y - BALL_SIZE / 2
                ):
            
            # collision 
            left_distance = x + BALL_SIZE - brick[0]
            right_distance = -(x - BALL_SIZE - brick[2])
            top_distance = y + BALL_SIZE - brick[1]
            bottom_distance = -(y - BALL_SIZE - brick[3])
            min_distance = min(left_distance, right_distance, top_distance, bottom_distance)
            
            if min_distance == left_distance:
                dirxX = 'left'
            elif min_distance == right_distance:
                dirxX = 'right'
            elif min_distance == top_distance:
                dirxY = 'top'
            elif min_distance == bottom_distance:
                dirxY = 'bottom'
            
            del bricks[i]
            break
            
        i += 1
            
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
    
def drawBricks():
    for brick in bricks:
        fill('#f1f1f1')
        rect(brick[0], brick[1], brick[2] - brick[0], brick[3] - brick[1])
            
    
