from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x1 < x0):
        draw_line(x1,y1,x0,y0,screen,color) #accounts for lines going other direction
        return
    dx = x1-x0
    dy = y1-y0
    #vertical
    if dx == 0:
        x,y = x0,y0
        if (dy > 0):
            while y < y1:
                plot(screen,color,x,y)
                y+=1
        else:
            while y > y1:
                plot(screen,color,x,y)
                y-=1
    #Octant 1,5 and 45deg & horrizontal
    if 0 <= dy <= dx:
        A = dy
        B = -1 * dx
        x,y = x0,y0
        d = 2*A + B
        while x <= x1:
            plot(screen,color,x,y)
            if d > 0:
                y+=1
                d+= 2 * B
            x+=1
            d+= 2 * A

    #Octant 2,6
    if 0 < dx < dy:
        A = dy
        B = -1 * dx
        x,y = x0,y0
        d = A + 2 * B
        while y <=y1:
            plot(screen,color,x,y)
            if d < 0:
                x+=1
                d+= 2 * A
            y+=1
            d+= 2 * B
    #Octant 7,3
    if dy < 0 and dy *-1 >= dx:
        #plot(screen,color,400,400)
        A = dy
        B = -1 * dx
        x,y = x0,y0
        d = A - 2 * B
        while y >= y1:
            plot(screen,color,x,y)
            if d > 0:
                x+=1
                d+= 2 * A
            y-=1
            d-= 2 * B
    #Octant 8,2
    if dy < 0 and (dy * -1) < dx:
        A = dy
        B = -1 * dx
        x,y = x0,y0
        d = 2*A - B
        while x <= x1:
            plot(screen,color,x,y)
            if d < 0:
                y-=1
                d-= 2 * B
            x+=1
            d+= 2 * A
