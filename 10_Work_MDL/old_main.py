from display import *
from draw import *
from parser import *
from matrix import *
import math


view = [0,
        0,
        1];
ambient = [50,
           50,
           50]
light = [[0.5,
          0.75,
          1],
         [0,
          255,
          255]]
areflect = [0.1,
            0.1,
            0.1]
dreflect = [0.5,
            0.5,
            0.5]
sreflect = [0.5,
            0.5,
            0.5]


screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 0, 0 ]
edges = []
polygons = []
transform = new_matrix()

parse_file( 'script', edges, polygons, transform, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
