from math import sin, cos, pi, sqrt

width = 50
for i in range(9):
    x = f"{cos(i*pi/16)*(width/2*sqrt(2))}px"
    y=f"-{sin(i*pi/16)*(width/2*sqrt(2))}px)"
    print(x,y)



