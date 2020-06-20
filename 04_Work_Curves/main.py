from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

def add_circle( cx, cy, r, step ):
    file = open("script2", "w")
    alpha = 2*math.pi / step

    x = cx + (r * math.cos(0))
    y = cy + (r * math.sin(0))

    t = 0
    radius = 20
    while t <= 2*math.pi:
        x2 = cx + (r * math.cos(t))
        y2 = cy + (r * math.sin(t))
        #print(x2, y2)
        file.write("circle\n")
        file.write(str(x2) + " " + str(y2) + " 0 " + str(radius) + "\n" )

        radius += 5
        x = x2
        y = y2
        t += alpha
    file.write("save\ncircles.png\n")
    file.close()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

#add_circle(250, 250, 90, 25)


parse_file( 'script', edges, transform, screen, color )
#parse_file( 'script2', edges, transform, screen, color )
