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

def parse_file( fname, edges, polygons, csystems, screen, zbuffer, color ):

    f = open(fname)
    lines = f.readlines()

    clear_screen(screen)
    clear_zbuffer(zbuffer)
    step = 100
    step_3d = 20

    c = 0
    while c < len(lines):
        line = lines[c].strip()
        #print ':' + line + ':'

        if line in ARG_COMMANDS:
            c+= 1
            args = lines[c].strip().split(' ')

        if line == 'push':
            csystems.append( [x[:] for x in csystems[-1]] )

        elif line == 'pop':
            csystems.pop()

        elif line == 'sphere':
            #print 'SPHERE\t' + str(args)
            add_sphere(polygons,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step_3d)
            matrix_mult(csystems[-1], polygons)
            draw_polygons(polygons, screen, zbuffer, color)
            polygons = []

        elif line == 'torus':
            #print 'TORUS\t' + str(args)
            add_torus(polygons,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), step_3d)
            matrix_mult(csystems[-1], polygons)
            draw_polygons(polygons, screen, zbuffer, color)
            polygons = []

        elif line == 'box':
            #print 'BOX\t' + str(args)
            add_box(polygons,
                    float(args[0]), float(args[1]), float(args[2]),
                    float(args[3]), float(args[4]), float(args[5]))
            matrix_mult(csystems[-1], polygons)
            draw_polygons(polygons, screen, zbuffer, color)
            polygons = []

        elif line == 'circle':
            #print 'CIRCLE\t' + str(args)
            add_circle(edges,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step)
            matrix_mult(csystems[-1], edges)
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
            matrix_mult(csystems[-1], edges)
            draw_lines(edges, screen, zbuffer, color)
            edges = []

        elif line == 'line':
            #print 'LINE\t' + str(args)
            add_edge( edges,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), float(args[5]) )
            matrix_mult(csystems[-1], edges)
            draw_lines(edges, screen, zbuffer, color)
            edges = []

        elif line == 'scale':
            #print 'SCALE\t' + str(args)
            t = make_scale(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(csystems[-1], t)
            csystems[-1] = [x[:] for x in t]


        elif line == 'move':
            #print 'MOVE\t' + str(args)
            t = make_translate(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(csystems[-1], t)
            csystems[-1] = [x[:] for x in t]

        elif line == 'rotate':
            #print 'ROTATE\t' + str(args)
            theta = float(args[1]) * (math.pi / 180)

            if args[0] == 'x':
                t = make_rotX(theta)
            elif args[0] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            matrix_mult(csystems[-1], t)
            csystems[-1] = [x[:] for x in t]

        elif line == 'ident':
            ident(transform)

        elif line == 'apply':
            matrix_mult( transform, edges )
            matrix_mult( transform, polygons )

        elif line == 'clear':
            clear_screen(screen)
            clear_zbuffer(zbuffer)

        elif line == 'display' or line == 'save':
            #clear_screen(screen)
            if line == 'display':
                display(screen)
            else:
                save_extension(screen, args[0])
        c+= 1
