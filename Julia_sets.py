from graphics import *
import math as m 
import cmath as cm
from matplotlib.cm import rainbow
import numpy as np

WIDTH = 500
HEIGHT = 500

def main():
	num_colors = 1000
	colormap = linear_gradient("#0000FF", "#FFFFFF", num_colors)
	print(len(colormap['r']))
	# print(colormap[])
	# print(colormap)
	win = GraphWin("My putnam WIndowww", WIDTH, HEIGHT)
	win.setBackground(color_rgb(0,0,0))
	print(cast_point(Point(0,0)))
	print(cast_point(Point(500,500)))
	print(cast_point(Point(500,0)))
	loop = True
	while loop:
		pt = win.checkMouse()
		# img = Image(Point(0,0),500,500)
		if pt:
			c = cast_point(pt)
			R = 16
			for i in range(WIDTH):
				for j in range(HEIGHT):
					z = cast_point(Point(i,j))
					max_iteration = num_colors
					iteration = 0
					print("Iterating z = {} ...".format(z))
					while (z.real**2 + z.imag**2 < R**2 and  iteration < max_iteration):
						# print("z = {}".format(z))
						z = z**2 + c
						iteration += 1
					print("Stop iteration: {}".format(iteration))
					if iteration == max_iteration:
						win.plot(i,j,color_rgb(0,0,0))
					else:
						iteration = rgb_stop(iteration*50)
						(r,g,b) = ( colormap['r'][iteration], 
									colormap['g'][iteration],
									colormap['b'][iteration]
								   )
						color = color_rgb(r,g,b)
						win.plot(i,j,color)
			# loop = False
			# img.draw(win)				

	win.getMouse()
	win.close()

def rgb_stop(r):
	if r >= 1000:
		return 999
	return r

# A function that throws a point on the screen to the complex plane C.
def cast_point(point):
	return complex((point.x-WIDTH/2)/WIDTH*4, (point.y-HEIGHT/2)/HEIGHT*4)
# A function that prints a complex point to a corresponding point 
# on the screen 
def print_point(point):
	return Point((point.x+1)*WIDTH/2, (point.y+1)*HEIGHT/2)

def hex_to_RGB(hex):
  ''' "#FFFFFF" -> [255,255,255] '''
  # Pass 16 to the integer function for change of base
  return [int(hex[i:i+2], 16) for i in range(1,6,2)]


def RGB_to_hex(RGB):
  ''' [255,255,255] -> "#FFFFFF" '''
  # Components need to be integers for hex to make sense
  RGB = [int(x) for x in RGB]
  return "#"+"".join(["0{0:x}".format(v) if v < 16 else
            "{0:x}".format(v) for v in RGB])
def color_dict(gradient):
  ''' Takes in a list of RGB sub-lists and returns dictionary of
    colors in RGB and hex form for use in a graphing function
    defined later on '''
  return {"hex":[RGB_to_hex(RGB) for RGB in gradient],
      "r":[RGB[0] for RGB in gradient],
      "g":[RGB[1] for RGB in gradient],
      "b":[RGB[2] for RGB in gradient]}


def linear_gradient(start_hex, finish_hex="#FFFFFF", n=10):
  ''' returns a gradient list of (n) colors between
    two hex colors. start_hex and finish_hex
    should be the full six-digit color string,
    inlcuding the number sign ("#FFFFFF") '''
  # Starting and ending colors in RGB form
  s = hex_to_RGB(start_hex)
  f = hex_to_RGB(finish_hex)
  # Initilize a list of the output colors with the starting color
  RGB_list = [s]
  # Calcuate a color at each evenly spaced value of t from 1 to n
  for t in range(1, n):
    # Interpolate RGB vector for color at the current value of t
    curr_vector = [
      int(s[j] + (float(t)/(n-1))*(f[j]-s[j]))
      for j in range(3)
    ]
    # Add it to our list of output colors
    RGB_list.append(curr_vector)

  return color_dict(RGB_list)

main()