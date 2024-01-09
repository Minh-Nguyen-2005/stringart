#Author: Minh Nguyen
#Date: 09/29/2023
#Purpose: Draw Virtual String Art

from cs1lib import *

#variables
OFFSET = 20
WIN_SIZE = 400
x = 0
y = 0
dx = OFFSET
dy = 0
draw_background = True

def draw_points(sx, sy): #simulate placing the thumbtacks along the outline.
    enable_stroke()
    set_stroke_width(4)
    set_stroke_color(1, 0, 0)
    draw_point(sx, sy)

def draw_lines(x1, y1, x2, y2): #draw a line between a pair of points on the outline.
    enable_stroke()
    set_stroke_width(1)
    set_stroke_color(0, 1, 1)
    draw_line(x1, y1, x2, y2)

def mydraw(): #main draw function
    global x, y, draw_background, dx, dy
    #clear background only the first time main draw function is called
    #to keep the lines drawn in previous calls to the main draw function.
    if draw_background == True: #
        set_clear_color(1, 1, 1)
        clear()
        draw_background = False

    #a pair of points needed to be connected
    draw_points(x, y)
    draw_points(y, WIN_SIZE - x)
    #a line connects that pair of points
    draw_lines(x, y, y, WIN_SIZE - x)

    #determine the distance moving the point (x, y) after turning around each corner of the square graphics window.
    if y == 0 and x < WIN_SIZE:
        dx = OFFSET
        dy = 0
    elif y < WIN_SIZE and x == WIN_SIZE:
        dx = 0
        dy = OFFSET
    elif y == WIN_SIZE and x > 0:
        dx = -OFFSET
        dy = 0
    else:
        dx = 0
        dy = -OFFSET
    x = x + dx
    y = y + dy

start_graphics(mydraw)