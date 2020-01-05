from graphics import *
import math as m 
import cmath as cm

def main():
	win = GraphWin("My putnam WIndowww", 500, 500)
	win.setBackground(color_rgb(255,0,0))
	pt = Point(250,250)
	cir = Circle(pt, 125)
	cir.setFill(color_rgb(100,255,50))
	cir.draw(win)
	while True:
		pt = win.checkMouse()
		if pt:
			cir = Circle(pt, 10)
			cir.setFill(color_rgb(100,255,50))
			cir.draw(win)

			print("Sequence:")
			last_pt = pt
			pt = cast_point(pt)
			c = complex(pt.x, pt.y)
			n = 30
			z = 1
			slice_angle = 2*m.pi/n

			for i in range(n):
				z = 1*m.e**(complex(0,slice_angle*i))
				z = (z + c)**2
				print(z)
				pt = print_point(Point(z.real, z.imag))
				print(pt)
				cir = Circle(pt, 10)
				cir.setFill(color_rgb(10+i*6,200-i*3,50+i*1))
				cir.draw(win)
				line = Line(last_pt, pt)
				line.draw(win)
				last_pt = pt


	win.getMouse()
	win.close()

def rgb_stop(r):
	if r >= 250:
		return 250
	return r


def cast_point(point):
	return Point((point.x-250)/125, (point.y-250)/125)
def print_point(point):
	return Point((point.x+1)*250, (point.y+1)*250)

main()