size(500, 500)
noStroke()
fill(128)
x = 0
while x < width:
    fill(x/2)
    rect(x, 0, 100, 100)
    x += 100
    
x = 50
while x < width:
    fill(255 - x / 2)
    ellipse(x, 200, 100, 100)
    x += 100
