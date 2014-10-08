# -*- coding: utf-8 -*-
"""
Random_art.py

@author: amonmillner, adapted from pruvolo work
"""

# you do not have to use these particular modules, but they may help
from random import randint
from PIL import Image
import math

# The following are the functions
def prod(a,b):
	return a * b

def cos_pi(a):
	return math.cos(math.pi*a)
	
def sin_pi(a):
	return math.sin(math.pi*a)
	
def cube(a, b, c):
	return a * b * c
	
def ellipse(a, b):
	e = ((a**2)/4)+((b**2)/4)
	return e

def circle(a):
	return math.pi * 2 * (a) 

def X(a,b):
	return a

def Y(a,b):
	return b

#	This is the recursive function that get called by the create random function. This
# 	is actually doing the random function generating.  
def build_list(n):
	if n == 1:
		return [rand_base()]
	else:
		func = rand_function()
		if func == 'prod':
			return [func, build_list(n - 1), build_list(n - 1)]
		if func == 'cube':
			return [func, build_list(n - 1), build_list(n - 1), build_list(n - 1)]
		if func == 'ellipse':
			return [func, build_list(n - 1), build_list(n - 1)]
		return [func, build_list(n - 1)]

#	This function spits out a base variable when called as a string.
def rand_base():
	x = randint(0, 1)
	if x == 0:
		return 'x'
	if x == 1:
		return 'y'

# 	This function spits out a random function as a string.		
def rand_function():
	x = randint(1, 6)
	if x == 1:
		return 'prod'
	if x == 2:
		return 'cos_pi'
	if x == 3:
		return 'sin_pi'
	if x == 4:
		return 'ellipse'
	if x == 5:
		return 'circle'
	if x == 6:
		return 'cube'

#	Chooses random depth then calls another function to do the actual generating. 	
def build_random_function(min_depth, max_depth):
	n = randint(int(min_depth), int(max_depth))
	s = build_list(n)
	return s

#	EVALUATE RANDOM FUNCTION, evaluates the function recursively. 
def erf(f, x, y):
	if (f[0] == 'x'):
		return X(x,y)
	if (f[0] == 'y'):
		return Y(x,y)
	if (f[0] == 'cos_pi'):
		return cos_pi(erf(f[1], x, y))
	if (f[0] == 'sin_pi'):
		return sin_pi(erf(f[1], x, y))
	if (f[0] == 'cube'):
		return cube(erf(f[1], x, y), erf(f[2], x, y), erf(f[3], x, y))
	if (f[0] == 'ellipse'):
		return ellipse(erf(f[1], x, y), erf(f[2], x, y))
	if (f[0] == 'circle'):
		return circle(erf(f[1], x, y))
	if (f[0] == 'prod'):
		return prod(erf(f[1], x, y), erf(f[2], x, y))

# iis = input interval start, iie = input interval end, ois = output interval start, oie = output interval end
def remap_interval(val, iis, iie, ois, oie):
	o = (oie - ois) * (val - iis) 
	o = o / (iie - iis)
	o = o + ois
	return float(o)
	
	""" Maps the input value that is in the interval [input_interval_start, input_interval_end]
    	to the output interval [output_interval_start, output_interval_end].  The mapping
		is an affine one (i.e. output = input*c + b).
        TODO: please fill out the rest of this docstring
    """
def create_gray(f, iis, iie, oix, oiy):
	imgg = Image.new("L", (int(oix), int(oiy)))
	width_x = float(iie - iis) / (oix)
	width_y = float(iie - iis) / (oiy)
	y = iis
	x = iis
	while (y <= iie):
		pixel_y = int(remap_interval(y, iis, iie, 0, oiy-1))
		while (x <= iie):
			i = erf(f, x, y)
			i_remap = int(remap_interval(i, -1, 1, 0, 255))
			pixel_x = int(remap_interval(x, iis, iie, 0, oix-1))
			imgg.putpixel((pixel_x, pixel_y), i_remap)
			x = x + width_x
		x = -1
		y = y + width_y
	return imgg

def create_picture(mind , maxd, ois, oie):
	r = build_random_function(mind, maxd)
	g = build_random_function(mind, maxd)
	b = build_random_function(mind, maxd)
	red = create_gray(r, -1, 1, ois, oie)
	green = create_gray(g, -1, 1, ois, oie)
	blue = create_gray(b, -1, 1, ois, oie)
	return Image.merge("RGB", (red, green, blue))
	#return {"image":Image.merge("RGB", (red, green, blue)), "red":r, "green": g, "blue":b}
			

minn = raw_input("Enter min Depth: ")
maxx = raw_input("Enter max Depth: ")
ois = raw_input("Enter out width: ")
oie = raw_input("Enter out height: ")
x = 0
for x in range(5):
	a = create_picture(minn, maxx, int(ois), int(oie))
	a.show()
	a.save("image-"+str(x), "PNG")
	


