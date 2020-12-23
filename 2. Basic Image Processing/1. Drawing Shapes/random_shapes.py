# Use a random number generator to draw random number of shapes in various sizes over the canvas
import random
import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_canvas(image, cmap = None, fig_size = (10,10)):
    fig, ax = plt.subplots(figsize=fig_size)
    ax.imshow(image, cmap = cmap)
    ax.axis('on')
    plt.show()

canvas = np.zeros((300, 300, 3), dtype="uint8")
display_canvas(canvas)

def pick_colour():
    colours = ["red", "green", "purple", "blue", "yellow", "brown", "white"]
    pick = random.choice(colours)
    if pick == "red":
        return (0, 0, 255)
    elif pick == "green":
        return (0 , 255, 0)
    elif pick == "blue":
        return (255, 0 , 0)
    elif pick == "yellow":
        return (67, 255, 211)
    elif pick == "brown":
        return (15, 54, 138)
    elif pick == "white":
        return (255, 255, 255)
    elif pick == "purple":
        return (139, 34, 104)


def pick_tickness(min, max):
    return random.randint(min, max)

def pick_coordinates(min, max):
    x = random.randint(min, max)
    y =  random.randint(min, max)
    return (x, y)

# generate random number, that will correspong to the number of shapes that will appear
# on the canvas. we will consider up to 10 shapes

num = random.randint(1,10)

curves_tickness = random.randint(-1, 5)
radius = random.randint(10,150)


if num <= 3:
    # draw something  2 lines and one shape
    cv2.circle(canvas, pick_coordinates(10, 200), radius, pick_colour(), curves_tickness)
    cv2.line(canvas, pick_coordinates(1, 300), pick_coordinates(0, 200), pick_colour(), 1)
    cv2.line( canvas, pick_coordinates(0, 200), pick_coordinates(0, 250), pick_colour(), pick_tickness(1, 7))

if num > 3 and num <= 5:
    # draw something 1 line, 1 rectangle and 1 circle
     cv2.line(canvas, pick_coordinates(23, 146), pick_coordinates(0, 300), pick_colour(), pick_tickness(3, 6))
     cv2.circle(canvas, pick_coordinates(10, 135), radius, pick_colour(), curves_tickness)
     cv2.line(canvas, pick_coordinates(0, 300), pick_coordinates(0, 244), pick_colour(), pick_tickness(6, 8))
     cv2.rectangle(canvas,pick_coordinates(100, 255), pick_coordinates(0, 300), pick_colour(), pick_tickness(1, 15))
if num > 5 and num <= 7:
    # draw something two circle, 2 rectangles
     cv2.circle(canvas, pick_coordinates(0, 300), radius, pick_colour(), curves_tickness)
     cv2.rectangle(canvas, pick_coordinates(0, 29), pick_coordinates(4, 266), pick_colour(), pick_tickness(1, 14))
     cv2.line(canvas,pick_coordinates(34, 100), pick_coordinates(2, 34), pick_colour(), 1)

if num > 7:
    #draw something else 1 circle, 1 rectangle, triangle and a line
     # Three vertices(tuples) of the triangle
     p1 = (100, 200)
     p2 = (50, 50)
     p3 = (300, 100)

     cv2.line(canvas, p1, p2, pick_colour(), 3)
     cv2.line(canvas, p2, p3, pick_colour(), 3)
     cv2.line(canvas, p1, p3, pick_colour(), 3)

     cv2.line( canvas,  pick_coordinates(3, 87),  pick_coordinates(0, 300), pick_colour(), pick_tickness(7, 10))
     cv2.circle(canvas, pick_coordinates(3, 200), radius, pick_colour(), curves_tickness)
     cv2.rectangle(canvas, pick_coordinates(0, 300), pick_coordinates(45, 245), pick_colour(), pick_tickness(4, 9))

display_canvas(np.flip(canvas, axis = 2))                                                                                                                         