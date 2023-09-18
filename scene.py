# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_sky(canvas,scene_width,scene_height, 335, "burlywood1")
    draw_sky(canvas,scene_width,scene_height, 300, "burlywood2")
    draw_sky(canvas,scene_width,scene_height, 250, "burlywood")
    draw_sky(canvas,scene_width,scene_height, 200, "salmon2")
    draw_sky(canvas,scene_width,scene_height, 150, "lightCoral")
    draw_sky(canvas,scene_width,scene_height, 100, "indianRed1")
    draw_sky(canvas,scene_width,scene_height, 50, "indianRed2") 
    diameter = 300
    x = scene_width / 3.15
    y = 100
    draw_oval(canvas, x, y, x + diameter, y + diameter, outline="lightYellow1", fill="lightYellow1")
    draw_ground(canvas,scene_width,scene_height)
 

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height, x , color):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height - x,
        scene_width, scene_height, width=0, fill=color)

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="skyBlue")
    draw_rectangle(canvas, 0, 0,
        scene_width, 115, width=0, fill="skyBlue2")
    draw_rectangle(canvas, 0, 0,
        scene_width, 65, width=0, fill="skyBlue3")    


        # Draw a pine tree.
    tree_center_x = scene_width / 2
    tree_bottom = 168
    tree_height = 120
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height 
    trunk_height = height / 6
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="gray20")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x +2, skirt_top - 10,
            skirt_right - 30, trunk_top ,
            skirt_left - 30, trunk_top + 10,
            outline="gray20", width=1, fill="gray20")
    

    draw_polygon(canvas, center_x + 3, skirt_top - 10,
            skirt_right+ 30, trunk_top+ 30,
            skirt_left+35, trunk_top +20, 
            outline="gray20", width=1, fill="gray20")

# Call the main function so that
# this program will start executing.
main()