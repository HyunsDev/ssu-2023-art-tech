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


def sun_ParkHyunWoo(x, y, sunColor="#FEEB61", isAnimationPlay=True, animationSpeed=1):
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
    fill("#000000")
    circle((x - 20) + distanceX, y + distanceY, 8)
    circle((x + 20) + distanceX, y + distanceY, 8)

    # draw mouse
    noStroke()
    fill("#FE967B")
    arc(x + distanceX * 2 / 3, y + 5 + distanceY / 2, 20, 20, 0, PI)

    # draw sunlight
    for i in range(8):
        pushMatrix()
        rectMode(CENTER)
        translate(x, y)

        if isAnimationPlay:
            rotate(PI / 4 * i + frameCount * PI / 360 * animationSpeed)
        else:
            rotate(PI / 4 * i)

        fill(sunColor)
        noStroke()
        rect(0, -65, 10, 30, 100)
        popMatrix()

    # load the orginal Style
    popStyle()


"""
"Draws cloud image

Parameters:
    x(int) : left top x
    y(int) : left top y
    c(color) : cloud color
    e(emotion) : type 1 or 2 / 1 -> smile , 2 -> sad
    d(direction) : type 1 or 2 / 1 ->original, 2->reverse left and right

Returns :
    None"
"""


def drawCloud_KimDoyeong(x, y, c, e, d):
    fill(c)
    if d == 1:
        rect(x + 60, y + 140, 260, 80)
        rect(x + 190, y + 100, 60, 40)
        ellipse(x + 60, y + 160, 120, 120)
        ellipse(x + 140, y + 80, 160, 160)
        ellipse(x + 260, y + 90, 130, 130)
        ellipse(x + 320, y + 170, 100, 100)

        # eye
        fill(0)
        circle(x + 70, y + 150, 8)
        circle(x + 120, y + 150, 8)

        if e == 1:
            # face1
            fill(250, 130, 130)
            arc(x + 95, y + 150, 20, 20, 0, PI, CHORD)
        elif e == 2:
            # face2
            fill(250, 130, 130)
            arc(x + 95, y + 160, 20, 20, PI, 2 * PI, CHORD)

    elif d == 2:
        rect(x + 60, y + 140, 260, 80)
        rect(x + 130, y + 100, 60, 40)
        ellipse(x + 320, y + 160, 120, 120)
        ellipse(x + 240, y + 80, 160, 160)
        ellipse(x + 120, y + 90, 130, 130)
        ellipse(x + 60, y + 170, 100, 100)

        # eye
        fill(0)
        circle(x + 310, y + 150, 8)
        circle(x + 260, y + 150, 8)

        if e == 1:
            # face1
            fill(250, 130, 130)
            arc(x + 285, y + 150, 20, 20, 0, PI, CHORD)
        elif e == 2:
            # face2
            fill(250, 130, 130)
            arc(x + 285, y + 160, 20, 20, PI, 2 * PI, CHORD)


def cat_YunaPyeoun(x, y, cat=4, w=50, h=50):
    """
    Draw various kinds of cats
    *It only works if you're connected to the Internet!
    *It takes a long time to load the cat for the first time,
    so it doesn't take a long time to load once it's loaded.


    Paramters:
        x(int) : left top x
        y(int) : left top y
        cat : Set cat type
          0. a gray cat
          1. a white cat
          2. a cheese cat
          3. a Siamese cat
          4. a three-colored cat
        w(int) : cat width
        h(int) : cat height

        Returns:
            None

    example code:
        1. to draw various kinds of cats
           cat_YunaPyeoun(100, 100, 0)
           cat_YunaPyeoun(200, 200, 1)
           cat_YunaPyeoun(300, 300, 3)
           cat_YunaPyeoun(400, 400, 4)

        2. change the size of a cat
           cat_YunaPyeoun(100, 100, 0, 100, 100)
           cat_YunaPyeoun(100, 100, 0, 300, 300)


    """
    global Img
    global image_cache

    # Don't modify it
    # Initialize image cache
    if "image_cache" not in globals():
        globals()["image_cache"] = {}

    if cat not in image_cache:
        cat_img = [
            "https://i.ibb.co/4m3LV7x/1.png",
            "https://i.ibb.co/3c3S0L7/2.png",
            "https://i.ibb.co/HPfRDzj/3.png",
            "https://i.ibb.co/1Z8pWwg/4.png",
            "https://i.ibb.co/L0vZWHd/7.png",
        ]
        image_cache[cat] = loadImage(cat_img[cat])

    Img = image_cache[cat]
    image(Img, x, y, w, h)


def cherryblossom_leeseonwoo(
    x,
    y,
    sz=100,
    petalcolor=color(245, 185, 215, 130),
    ovarycolor=color(225, 40, 90),
    linecolor=color(211, 65, 120),
):
    stamenangle = [
        276.1471862792969,
        109.93315124511719,
        96.10581970214844,
        244.46124267578125,
        33.7631950378418,
        157.9586944580078,
        323.84814453125,
        340.3305969238281,
        128.58082580566406,
        64.87469482421875,
    ]
    stamenl = [
        89.33432698249817,
        118.21951866149902,
        83.44976305961609,
        104.71519231796265,
        111.06138229370117,
        122.60611057281494,
        118.16256046295166,
        97.83667922019958,
        118.75615119934082,
        85.53948998451233,
    ]

    def petal(angle, petalcolor, sz=sz):
        noFill()
        strokeWeight(6)
        stroke(petalcolor)

        pushMatrix()
        translate(x, y)
        rotate(radians(angle))
        for cx in range(-sz, sz + 5, 5):
            bezier(0, 0, cx, -0.7 * sz, cx, -2 * sz, 0, -2 * sz)
        popMatrix()

    def stamen(i):
        stroke(linecolor)
        angle = stamenangle[i]
        pushMatrix()
        translate(x, y)
        rotate(radians(angle))
        l = stamenl[i]
        line(0, 0, 0, l)
        noStroke()
        fill(255, 212, 121)
        circle(0, l, sz / 10)
        popMatrix()

    for i in range(5):  # draw petal
        petal(72 * i, petalcolor)

    for i in range(5):  # draw ovary
        petal(72 * i, color(225, 40, 90), 10)

    fill(160, 0, 60)
    circle(x, y, sz / 5)
    strokeWeight(2)

    for i in range(10):  # draw stamen
        stamen(i)
