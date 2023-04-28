

"""
Draw Animatied Sun

    functions:
        1. sunlight is spin
        2. sun looks at the mouse

    Paramters: 
        x (int): left top x
        y (int): left top y
        sunColor (color, string): sun color ( default: '#FEEB61' )
        isAnimationPlay (bool): is play animation ( default: True )
        animationSpeed (int): degree to increase for 1 frame ( default: 1 )
        
    Returns:
        None
        
    example:
        1 default: sun_ParkHyunWoo(width - 100, 100)
        2 change Color: sun_ParkHyunWoo(width - 100, 100, sunColor = '#ff0000')
        3 change all option: sun_ParkHyunWoo(width - 100, 100, sunColor = '#ff0000', isAnimationPlay = False, animationSpeed = 30)
        4 change all option: sun_ParkHyunWoo(width - 100, 100, '#ff0000', False, 30)
        # 3 == 4
"""
def sun_ParkHyunWoo(x, y, sunColor = '#FEEB61', isPlay = True, animationSpeed = 1):
    # Save the orginal Style
    pushStyle()

    # distance sun and mouse
    # -10 <= value <= 10
    distanceX = map(mouseX - x, -width, width, -10, 10)
    distanceY = map(mouseY - y, -height, height, -10, 10)
    
    # draw sun body
    noStroke()
    fill(sunColor)
    circle(x + distanceX / 4, y + distanceY / 4, 80)
    
    # draw eyes
    noStroke()
    fill('#000000')
    circle((x - 20) + distanceX, y + distanceY, 8)
    circle((x + 20) + distanceX, y + distanceY, 8)
    
    # draw mouse
    noStroke()
    fill('#FE967B')
    arc(x + distanceX * 2/3, y + 5 + distanceY / 2, 20, 20, 0, PI)
    
    # draw sunlight
    for i in range(8):
        pushMatrix()
        rectMode(CENTER)
        translate(x, y)
        
        if isPlay:
            rotate(PI/4*i + frameCount * PI/360 * animationSpeed)
        else:
            rotate(PI/4*i)
        
        fill(sunColor)
        noStroke()
        rect(0, -65, 10, 30, 100)
        popMatrix()
        
    # load the orginal Style
    popStyle()

def setup():
    size(500, 500)
    
def draw():
    background('#ffffff')
    sun_ParkHyunWoo(width - 100, 100, animationSpeed = 20)
    sun_ParkHyunWoo(width - 100, height-100, sunColor = '#80FE61')
    sun_ParkHyunWoo(100, height - 100, isPlay = False)
    sun_ParkHyunWoo(100, 100)
    sun_ParkHyunWoo(width / 2, height / 2)
    
    pass
