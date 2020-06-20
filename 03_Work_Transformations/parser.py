from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname,"r")
    lines = file.read().split("\n")
    print(lines)
    counter = 0
    while counter < len(lines):
        if lines[counter] == "line":
            args = lines[counter + 1].split(" ")
            add_edge(points,int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
            counter += 2
        elif lines[counter] == "ident":
            ident(transform)
            counter += 1
        elif lines[counter] == "scale":
            args = lines[counter + 1].split(" ")
            scale = make_scale(int(args[0]), int(args[1]), int(args[2]))
            matrix_mult(scale, transform)
            counter += 2
        elif lines[counter] == "move":
            args = lines[counter + 1].split(" ")
            translate = make_translate(int(args[0]), int(args[1]), int(args[2]))
            matrix_mult(translate, transform)
            counter += 2
        elif lines[counter] == "rotate":
            args = lines[counter + 1].split(" ")
            axis = args[0]
            num = int(args[1])
            if (axis == "x"):
                rot = make_rotX(num)
            elif (axis == "y"):
                rot = make_rotY(num)
            else:
                rot = make_rotZ(num)
            matrix_mult(rot, transform)
            counter += 2
        elif lines[counter] == "apply":
            matrix_mult(transform, points)
            counter += 1
        elif lines[counter] == "display":
            clear_screen(screen)
            print_matrix(points)
            draw_lines( points, screen, color)
            display( screen )
            counter += 1
        elif lines[counter] == "save":
            clear_screen(screen)
            draw_lines( points, screen, color)
            save_extension( screen, lines[counter + 1])
            counter += 1
        elif lines[counter] == "quit":
            counter = len(lines)
        else:
            counter += 1

    #pass
