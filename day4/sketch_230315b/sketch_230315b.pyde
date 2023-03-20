
i = 0
is_go = False
rgb_r = 0
rgb_g = 125
rgb_b = 255

def setup():
    size(500, 500)
    
def draw():
    background(255)
    
    global i, is_go
    
    if is_go:
        i += 1
    else:
        i -= 1
        
    if i > 255 and is_go :
        is_go = False

    if i < 0 and not is_go :
        is_go = True
        
    line(0, 0, i, i)
    
    fill(i, i, i)
    circle(250,250,i)
