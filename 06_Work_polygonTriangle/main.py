from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()

def script2():
    file = open("script2", "w")
    counter = 0
    x = 75
    y = 150
    z = 50
    while counter < 4:
        file.write("box\n")
        file.write(str(x) + " " + str(y) + " " + str(z) + " 76 76 76\n")
        file.write("sphere\n")
        file.write(str(x + 38) + " " + str(y + 58) + " " + str(z - 38) +" 38\n")
        if counter == 3:
            file.write("torus\n")
            file.write(str(x + 77) + " " + str(y + 58 + 58) + " " + str(z - 77) +" 5 41\n")
        x += 152
        counter += 1

    file.write("ident\nrotate\ny 45\nrotate\nx 15\napply\n")
    file.write("save\nBoxes.png\n")
    file.close()
#script2()
#parse_file( 'script2', edges, polygons, transform, screen, color )
parse_file( 'script', edges, polygons, transform, screen, color )
