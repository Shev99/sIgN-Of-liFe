from display import *
from draw import *
from parser import *
from matrix import *
import math
from sys import argv

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()

if len(argv) != 2:
  parse_file( 'script', edges, polygons, transform, screen, zbuffer, color )
else:
  parse_file( argv[1], edges, polygons, transform, screen, zbuffer, color )
