from display import *
from draw import *

screen = new_screen()
"""
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
"""
#display(screen)

R = 128
G = 128
B = 0

while i < 500:
    color = [R,G,B]
    draw_line(i,500, 500-i, 0,screen,color)
    i+= 10

save_extension(screen, 'img.png')
