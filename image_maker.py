from Julia_sets import linear_gradient, Point, rgb_stop, color_dict
from PIL import Image
import numpy as np
# from itertools import tee, zip, chain

WIDTH = 500
HEIGHT = 700


def color_map(color_list):
    num_colors = 1000
    colormap = []
    for i, color in enumerate(color_list):
        if i < len(color_list) - 1:
            colormap += linear_gradient(color_list[i], color_list[i+1], num_colors)
    color_dict = color_dict( colormap )
    return color_dict


def draw_julia_set(width, height, color_list, c):
    pixels = [[(0, 0, 0) for i in range( height )] for j in range( width )]
    colormap = color_map(color_list)
    # print(colormap)
    # num_colors = len(colormap)
    num_colors = 1000
    pt = Point( 0, 0 )
    # c = complex( 1, 0 )
    R = 16
    print( 'jow' )
    for i in range( width ):
        for j in range( height ):
            z = cast_point( Point( i, j ) )
            max_iteration = num_colors
            iteration = 0
            # print( "Iterating z = {} ...".format( z ) )
            while z.real ** 2 + z.imag ** 2 < R ** 2 and iteration < max_iteration:
                z = z ** 2 + c
                iteration += 1
            # print( "Stop iteration: {}".format( iteration ) )
            if iteration == max_iteration:
                (r, g, b) = (0, 255, 0)
            else:
                overshoot = int(z.real ** 2 + z.imag ** 2 - R**2)
                # print(overshoot)
                iteration = rgb_stop( iteration * 300 + overshoot )
                (r, g, b) = (colormap['r'][iteration],
                             colormap['g'][iteration],
                             colormap['b'][iteration],
                             )
            pixels[i][j] = (r, g, b)
    # Convert the pixels into an array using numpy
    array = np.array( pixels, dtype=np.uint8 )
    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray( array )
    new_image.save( 'hejhoj.png' )


# A function that throws a point on the screen to the complex plane C.
def cast_point(point):
    return complex( (point.x - WIDTH / 2) / WIDTH * 4, (point.y - HEIGHT / 2) / HEIGHT * 4 )


# A function that prints a complex point to a corresponding point
# on the screen
def print_point(point):
    return Point( (point.x + 1) * WIDTH / 2, (point.y + 1) * HEIGHT / 2 )


color_list = ['#0000FF', '#FF0000', '#00FF00', "#000000"]
c = complex( 1, 0 )
draw_julia_set(WIDTH, HEIGHT, color_list, c)
