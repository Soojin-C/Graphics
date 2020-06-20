from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:

         push: push a copy of the current top of the coordinate system stack to the stack

         pop: pop off the current top of the coordinate system stack

         All the shape commands work as follows:
             1) Add the shape to a temporary matrix
             2) Multiply that matrix by the current top of the coordinate system stack
             3) Draw the shape to the screen
             4) Clear the temporary matrix

         sphere: add a sphere -
                 takes 4 arguemnts (cx, cy, cz, r)
         torus: add a torus -
                takes 5 arguemnts (cx, cy, cz, r1, r2)
         box: add a rectangular prism -
              takes 6 arguemnts (x, y, z, width, height, depth)

         circle: add a circle -
                 takes 3 arguments (cx, cy, r)
         hermite: add a hermite curve -
                  takes 8 arguments (x0, y0, x1, y1, rx0, ry0, rx1, ry1)
         bezier: add a bezier curve -
                 takes 8 arguments (x0, y0, x1, y1, x2, y2, x3, y3)
         line: add a line -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)

         All the transformation commands work as follows:
             1) Create the appropriate transformation matrix
             2) Multiply that matrix by current top of the coordinate system stack

         scale: takees 3 arguments (sx, sy, sz)
         move:  takes 3 arguments (tx, ty, tz)
         rotate: takes 2 arguments (axis, theta) axis should be x, y or z

         display: display the screen
         save: save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
ARG_COMMANDS = [ 'line', 'scale', 'move', 'rotate', 'save', 'circle', 'bezier', 'hermite', 'box', 'sphere', 'torus' ]

def parse_file( fname, edges, polygons, transform, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect ):

    f = open(fname)
    lines = f.readlines()

    clear_screen(screen)
    clear_zbuffer(zbuffer)
    t = new_matrix()
    ident(t)
    systems = [ t ]

    step = 100
    step_3d = 40

    c = 0
    while c < len(lines):
        line = lines[c].strip()
        #``print ':' + line + ':'

        if line in ARG_COMMANDS:
            c+= 1
            args = lines[c].strip().split(' ')
            #print 'args\t' + str(args)

        if line == 'sphere':
            #print 'SPHERE\t' + str(args)
            add_sphere(polygons,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step_3d)
            matrix_mult( systems[-1], polygons )
            draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
            polygons = []

        elif line == 'torus':
            #print 'TORUS\t' + str(args)
            add_torus(polygons,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), step_3d)
            matrix_mult( systems[-1], polygons )
            draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
            polygons = []

        elif line == 'box':
            #print 'BOX\t' + str(args)
            add_box(polygons,
                    float(args[0]), float(args[1]), float(args[2]),
                    float(args[3]), float(args[4]), float(args[5]))
            matrix_mult( systems[-1], polygons )
            draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
            polygons = []

        elif line == 'circle':
            #print 'CIRCLE\t' + str(args)
            add_circle(edges,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step)
            matrix_mult( systems[-1], edges )
            draw_lines(edges, screen, zbuffer, color)
            edges = []

        elif line == 'hermite' or line == 'bezier':
            #print 'curve\t' + line + ": " + str(args)
            add_curve(edges,
                      float(args[0]), float(args[1]),
                      float(args[2]), float(args[3]),
                      float(args[4]), float(args[5]),
                      float(args[6]), float(args[7]),
                      step, line)
            matrix_mult( systems[-1], edges )
            draw_lines(edges, screen, zbuffer, color)
            edges = []

        elif line == 'line':
            #print 'LINE\t' + str(args)

            add_edge( edges,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), float(args[5]) )
            matrix_mult( systems[-1], edges )
            draw_lines(eges, screen, zbuffer, color)
            edges = []

        elif line == 'scale':
            #print 'SCALE\t' + str(args)
            t = make_scale(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult( systems[-1], t )
            systems[-1] = [ x[:] for x in t]

        elif line == 'move':
            #print 'MOVE\t' + str(args)
            t = make_translate(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult( systems[-1], t )
            systems[-1] = [ x[:] for x in t]

        elif line == 'rotate':
            #print 'ROTATE\t' + str(args)
            theta = float(args[1]) * (math.pi / 180)
            if args[0] == 'x':
                t = make_rotX(theta)
            elif args[0] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            matrix_mult( systems[-1], t )
            systems[-1] = [ x[:] for x in t]

        elif line == 'push':
            systems.append( [x[:] for x in systems[-1]] )

        elif line == 'pop':
            systems.pop()

        elif line == 'display' or line == 'save':
            if line == 'display':
                display(screen)
            else:
                save_extension(screen, args[0])
        c+= 1
