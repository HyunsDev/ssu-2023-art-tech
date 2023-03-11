size(500, 500)

# line
P1 = [141, 176]
P2 = [294, 130]
P3 = [94, 279]
P4 = [199, 279]
P5 = [389, 279]

def pLine(point1, point2):
    line(point1[0], point1[1], point2[0], point2[1])
    
def pTri(p1, p2, p3):
    triangle(p1[0], p1[1], p2[0], p2[1], p3[0], p4[1])

background('#1f1f1f')

# line
strokeWeight(2)
stroke('#fe625e')
pLine(P1, P3)
stroke('#e14947')
pLine(P1, P4)
stroke('#9f458a')
pLine(P1, P5)
stroke('#f5aa80')
pLine(P2, P3)
stroke('#51e0fd')
pLine(P2, P4)
stroke('#51cdfd')
pLine(P2, P5)
stroke('#e58f93')
pLine(P3, P5)

# text
textSize(32)
text("Global Media", 140, 320)
