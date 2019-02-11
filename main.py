from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#display(screen)
draw_line(250,250,250,400,screen,color) #vertical up
draw_line(250,250,250,100,screen,color) #vertical down
draw_line(250,250,400,250,screen,color) #horrizontal left
draw_line(250,250,100,250,screen,color) #horrizontal left

color = [ 255, 0, 0 ]

draw_line(250,250,400,400,screen,color) #slope 1 up
draw_line(250,250,100,100,screen,color) #slope 1 down
draw_line(250,250,100,400,screen,color) #slope -1 up
draw_line(250,250,400,100,screen,color) #slope -1 down

color = [ 0, 0, 255]

draw_line(250,250,400,325,screen,color) #octant 1
draw_line(250,250,100,175,screen,color) #octant 5
draw_line(250,250,325,400,screen,color) #octant 2
draw_line(250,250,175,100,screen,color) #octant 6
draw_line(250,250,400,175,screen,color) #octant 8
draw_line(250,250,100,325,screen,color) #octant 4
draw_line(250,250,325,100,screen,color) #octant 7
draw_line(250,250,175,400,screen,color) #octant 3

display(screen)
"""
R = 256
G = 128
B = 0
i = 0
while i < 500:
    R = (R + 10) % 256
    G = (G + 10) % 256
    B = (B + 10) % 256
    color = [R,G,B]
    draw_line(i,500, 500-i, 0,screen,color)
    i+= 2
    color = [B,R,G]
    draw_line(500,i,0,500-i,screen,color)
    i+= 2
p = 0
while p < 250:
    color = [R,0,0]
    draw_line(p,p,p,500-p,screen,color)
    draw_line(p,p,500-p,p,screen,color)
    color = [0,0,B]
    draw_line(500-p,p,500-p,500-p,screen,color)
    draw_line(p,500-p,500-p,500-p,screen,color)
    p += 25
    R -= 15
    B -= 15
"""

save_extension(screen, 'img.png')
