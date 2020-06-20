from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:

         sphere: add a sphere to the POLYGON matrix -
                 takes 4 arguemnts (cx, cy, cz, r)
         torus: add a torus to the POLYGON matrix -
                takes 5 arguemnts (cx, cy, cz, r1, r2)
         box: add a rectangular prism to the POLYGON matrix -
              takes 6 arguemnts (x, y, z, width, height, depth)
         clear: clears the edge and POLYGON matrices

	 circle: add a circle to the edge matrix -
	         takes 4 arguments (cx, cy, cz, r)
	 hermite: add a hermite curve to the edge matrix -
	          takes 8 arguments (x0, y0, x1, y1, rx0, ry0, rx1, ry1)
	 bezier: add a bezier curve to the edge matrix -
	         takes 8 arguments (x0, y0, x1, y1, x2, y2, x3, y3)
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
               then multiply the transform matrix by the translation matrix -
               takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge and POLYGON matrices
         display: clear the screen, then
                  draw the lines of the edge and POLYGON matrices to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge and POLYGON matrices to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
ARG_COMMANDS = [ 'box', 'sphere', 'torus', 'circle', 'bezier', 'hermite', 'line', 'scale', 'move', 'rotate', 'save' ]

def parse_file( fname, edges, polygons, transform, screen, color ):

    f = open(fname)
    lines = f.readlines()

    step = 100
    step_3d = 20

    c = 0
    while c < len(lines):
        line = lines[c].strip()
        #print ':' + line + ':'

        if line in ARG_COMMANDS:
            c+= 1
            args = lines[c].strip().split(' ')

        if line == 'sphere':
            #print 'SPHERE\t' + str(args)
            add_sphere(edges,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step_3d)

        elif line == 'torus':
            #print 'TORUS\t' + str(args)
            add_torus(edges,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), step_3d)

        elif line == 'box':
            #print 'BOX\t' + str(args)
            add_box(polygons,
                    float(args[0]), float(args[1]), float(args[2]),
                    float(args[3]), float(args[4]), float(args[5]))

        elif line == 'circle':
            #print 'CIRCLE\t' + str(args)
            add_circle(edges,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step)

        elif line == 'hermite' or line == 'bezier':
            #print 'curve\t' + line + ": " + str(args)
            add_curve(edges,
                      float(args[0]), float(args[1]),
                      float(args[2]), float(args[3]),
                      float(args[4]), float(args[5]),
                      float(args[6]), float(args[7]),
                      step, line)

        elif line == 'line':
            #print 'LINE\t' + str(args)

            add_edge( edges,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), float(args[5]) )

        elif line == 'scale':
            #print 'SCALE\t' + str(args)
            t = make_scale(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(t, transform)

        elif line == 'move':
            #print 'MOVE\t' + str(args)
            t = make_translate(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(t, transform)

        elif line == 'rotate':
            #print 'ROTATE\t' + str(args)
            theta = float(args[1]) * (math.pi / 180)

            if args[0] == 'x':
                t = make_rotX(theta)
            elif args[0] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            matrix_mult(t, transform)

        elif line == 'ident':
            ident(transform)

        elif line == 'apply':
            if len(edges) > 0:
                matrix_mult( transform, edges )
            if len(polygons) > 0:
                matrix_mult( transform, polygons )

        elif line == 'clear':
            edges = []
            polygons = []

        elif line == 'display' or line == 'save':
            clear_screen(screen)
            if len(edges) > 0:
                draw_lines(edges, screen, color)
            if len(polygons) > 0:
                #for each in polygons:
                #    print(each)
                draw_polygons(polygons, screen, color)

            if line == 'display':
                display(screen)
            else:
                save_extension(screen, args[0])

        c+= 1
