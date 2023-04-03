size(600, 600)
background(255,255,255)

x = 110

while x < 600:
    stroke(255,0,0)
    strokeWeight(10)
    line(x, 0, x, 600)
    
    stroke(0,255,0)
    strokeWeight(10)
    line(x+10, 0, x+10, 600)
    
    stroke(255,255,0)
    strokeWeight(10)
    line(0, 0 - 300 + x, 600, 600 - 300 + x)
    
    stroke(255,0,255)
    strokeWeight(10)
    line(0, 600 + 300 - x, 600, 300 - x)
    
    x += 100
