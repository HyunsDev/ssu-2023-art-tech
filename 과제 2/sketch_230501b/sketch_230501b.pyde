import random
from functions import (
    sun_ParkHyunWoo,
    drawCloud_KimDoyeong,
    cat_YunaPyeoun,
    cherryblossom_leeseonwoo,
)


CLOUD_SPEED = 3
cloudX = 0
cloudAx = CLOUD_SPEED

# { x: int, y: int }
rains = []


def setup():
    size(600, 600)


isAngry = False


def draw():
    global isAngry
    global cloudX, cloudAx

    isAngry = mousePressed

    # Sun
    background("#ff8888" if isAngry else "#ffffff")
    sun_ParkHyunWoo(
        width - 100,
        100,
        sunColor="#FF0000" if isAngry else "#FEEB61",
        animationSpeed=40 if isAngry else 1,
    )

    # Cat
    cat_YunaPyeoun(450, 450, 4, 100, 100)
    cat_YunaPyeoun(380, 450, 3, 100, 100)
    cat_YunaPyeoun(300, 450, 2, 100, 100)
    cat_YunaPyeoun(220, 450, 1, 100, 100)

    # Cherry
    pushMatrix()
    scale(0.1)

    if not isAngry and frameCount % 60 == 0:
        rains.append(
            {"x": random.randrange((cloudX + 50) / 2, (cloudX + 350) / 2), "y": 220}
        )

    if isAngry and frameCount % 5 == 0:
        rains.append(
            {"x": random.randrange((cloudX + 50) / 2, (cloudX + 350) / 2), "y": 220}
        )

    for rain in rains:
        rain["y"] += 5
        if rain["y"] > height:
            rains.remove(rain)
        cherryblossom_leeseonwoo(rain["x"] * 10, rain["y"] * 10)

    popMatrix()

    strokeWeight(5)
    stroke(0)

    # Cloud
    pushMatrix()
    scale(0.5)
    noStroke()
    drawCloud_KimDoyeong(
        cloudX,
        200,
        "#666666" if isAngry else 0xFFC6EEF5,
        2 if isAngry else 1,
        2 if cloudAx > 0 else 1,
    )
    popMatrix()

    if isAngry:
        cloudX = cloudX + cloudAx * 4
    else:
        cloudX += cloudAx

    if cloudX > width - 100:
        cloudAx = -CLOUD_SPEED
    elif cloudX < 100:
        cloudAx = CLOUD_SPEED
