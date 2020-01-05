from Julia_sets import linear_gradient, Point, rgb_stop, color_dict
from PIL import Image
import numpy as np

WIDTH = 500
HEIGHT = 700


def fractal_draw():
    pixels = [[(0,0,0) for i in range(HEIGHT)] for j in range(WIDTH)]
    print(len(pixels))
    print(len(pixels[0]))
    num_colors = 1000
    colormap = linear_gradient( "#0000FF", "#FF00FF", num_colors )
    colormap += linear_gradient( "#FF00FF", "#FF0000", num_colors )
    colormap += linear_gradient( "#FF0000", "#FFFFFF", num_colors )
    colormap = color_dict(colormap)
    pt = Point(0,0)
    c = complex(1,0)
    R = 16
    print('jow')
    for i in range( WIDTH ):
        for j in range( HEIGHT ):
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
                iteration = rgb_stop( (iteration + 10) * 70 )
                (r, g, b) = (colormap['r'][iteration],
                             colormap['g'][iteration],
                             colormap['b'][iteration],
                             )
            pixels[i][j] = (r, g, b)
    # Convert the pixels into an array using numpy
    array = np.array( pixels, dtype=np.uint8 )
    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray( array )
    new_image.save( 'nej.png' )


# A function that throws a point on the screen to the complex plane C.
def cast_point(point):
    return complex((point.x - WIDTH / 2) / WIDTH * 4, (point.y - HEIGHT / 2) / HEIGHT * 4)


# A function that prints a complex point to a corresponding point
# on the screen
def print_point(point):
    return Point((point.x + 1) * WIDTH / 2, (point.y + 1) * HEIGHT / 2)


fractal_draw()
