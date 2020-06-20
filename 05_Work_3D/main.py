from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )
def script2():
    file = open("script2", "w")
    counter = 0
    x = 0
    y = 150
    z = 50
    while counter < 4:
        file.write("box\n")
        file.write(str(x) + " " + str(y) + " " + str(z) + " 50 50 50\n")
        count = 0
        while count < 4:
            z += 100
            file.write("box\n")
            file.write(str(x) + " " + str(y) + " " + str(z) + " 50 50 50\n")
            count += 1
        z = 50
        x += 100
        counter += 1
    counter = 0
    x = 100
    y = 200
    z = 100
    file.write("ident\nrotate\ny 45\nrotate\nx 15\napply\n")
    file.write("save\ncircles.png\n")
    file.close()


#script2()
#parse_file( 'script2', edges, transform, screen, color )

parse_file( 'script', edges, transform, screen, color )
