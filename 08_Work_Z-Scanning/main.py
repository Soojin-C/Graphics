from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 0, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]

def script2():
    file = open("script2", "w")
    counter = 0
    x = 0
    y = 150
    z = 50
    file.write("push\n")
    file.write("rotate\nx 15\nrotate\ny 45\n")
    while counter < 4:
        file.write("box\n")
        file.write(str(x) + " " + str(y) + " " + str(z) + " 50 50 50\n")
        count = 0
        while count < 3:
            z += 100
            file.write("box\n")
            file.write(str(x) + " " + str(y) + " " + str(z) + " 50 50 50\n")
            count += 1
        z = 50
        x += 100
        counter += 1
    counter = 0
    x = 50
    y = 200
    z = 100
    while counter < 3:
        file.write("box\n")
        file.write(str(x) + " " + str(y) + " " + str(z) + " 50 50 50\n")
        count = 0
        while count < 2:
            z += 100
            file.write("box\n")
            file.write(str(x) + " " + str(y) + " " + str(z) + " 50 50 50\n")
            count += 1
        z = 100
        x += 100
        counter += 1
    counter = 0
    x = 100
    y = 250
    z = 150
    while counter < 2:
        file.write("box\n")
        file.write(str(x) + " " + str(y) + " " + str(z) + " 50 50 50\n")
        count = 0
        while count < 1:
            z += 100
            file.write("box\n")
            file.write(str(x) + " " + str(y) + " " + str(z) + " 50 50 50\n")
            count += 1
        z = 150
        x += 100
        counter += 1
    x = 150
    y = 300
    z = 200
    file.write("box\n")
    file.write(str(x) + " " + str(y) + " " + str(z) + " 50 50 50\n")
    file.write("pop\n")
    file.write("save\nboxes.png\n")
    file.close()

#script2()
#parse_file('script2', edges, polygons, csystems, screen, zbuffer, color )
parse_file( 'script', edges, polygons, csystems, screen, zbuffer, color )
