from display import *
from matrix import *

  # ====================
  # add the points for a rectagular prism whose
  # upper-left corner is (x, y, z) with width,
  # height and depth dimensions.
  # ====================
def add_box( points, x, y, z, width, height, depth ):
    X = x + width
    Y = y - height
    d = z - depth
    # u_r = [X, y, z]
    # l_l = [x, Y, z]
    # l_r = [X, Y, z]

    # u_r2 = [u_r[0], u_r[1], d]
    # l_l2 = [l_l[0], l_l[1], d]
    # l_r2 = [l_r[0], l_r[1], d]

    add_edge(points, x, y, z, X, y, z)
    add_edge(points, X, y, z, X, Y, z)
    add_edge(points, X, Y, z, x, Y, z)
    add_edge(points, x, Y, z, x, y, z)

    add_edge(points, x, y, d, X, y, d)
    add_edge(points, X, y, d, X, Y, d)
    add_edge(points, X, Y, d, x, Y, d)
    add_edge(points, x, Y, d, x, y, d)

    add_edge(points, x, y, z, x, y, d)
    add_edge(points, X, y, z, X, y, d)
    add_edge(points, X, Y, z, X, Y, d)
    add_edge(points, x, Y, z, x, Y, d)

    #print(points)
    #pass

  # ====================
  # Generates all the points along the surface
  # of a sphere with center (cx, cy, cz) and
  # radius r.
  # Returns a matrix of those points
  # ====================
def generate_sphere( points, cx, cy, cz, r, step ):
    ret_matrix = []
    step2 = step / 2
    count = 0
    while count < step:
        counter = 0
        while counter < step2:
            theta = counter * ((2 * math.pi) / step)
            phi = count * ((2 * math.pi) / step)
            x = r * math.cos(theta) + cx
            y = r * math.sin(theta) * math.cos(phi) + cy
            z = r * math.sin(theta) * math.sin(phi) + cz

            add_point(ret_matrix, x, y, z)
            counter += 1
        count += 1
    #print(ret_matrix)
    return ret_matrix

    #pass

  # ====================
  # adds all the points for a sphere with center
  # (cx, cy, cz) and radius r to points
  # should call generate_sphere to create the
  # necessary points
  # ====================
def add_sphere( points, cx, cy, cz, r, step ):
    sphere_points = generate_sphere(points, cx, cy, cz, r, step)
    for each in sphere_points:
        x = each[0]
        y = each[1]
        z = each[2]
        add_edge(points, x, y, z, x+1, y+1, z+1)
    #pass


  # ====================
  # Generates all the points along the surface
  # of a torus with center (cx, cy, cz) and
  # radii r0 and r1.
  # Returns a matrix of those points
  # ====================
def generate_torus( points, cx, cy, cz, r0, r1, step ):
    count = 0
    ret_matrix = []
    while count < step:
        counter = 0
        while counter < step:
            theta = counter * ((2 * math.pi) / step)
            phi = count * ((2 * math.pi) / step)

            val1 = r0 * math.cos(theta) + r1
            x = (val1) * (math.cos(phi)) + cx
            y = (r0 * math.sin(theta)) + cy
            z = (val1) * (-1) * (math.sin(phi)) + cz
            add_point(ret_matrix, x, y, z)

            counter += 1
        count += 1
    return ret_matrix
    #pass

  # ====================
  # adds all the points for a torus with center
  # (cx, cy, cz) and radii r0, r1 to points
  # should call generate_torus to create the
  # necessary points
  # ====================
def add_torus( points, cx, cy, cz, r0, r1, step ):
    torus_points = generate_torus(points, cx, cy, cz, r0, r1, step)
    for each in torus_points:
        x = each[0]
        y = each[1]
        z = each[2]
        add_edge(points, x, y, z, x+1, y+1, z+1)
    #pass



def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy

    i = 1
    while i <= step:
        t = float(i)/step
        x1 = r * math.cos(2*math.pi * t) + cx;
        y1 = r * math.sin(2*math.pi * t) + cy;

        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        t+= step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    i = 1
    while i <= step:
        t = float(i)/step
        x = t * (t * (xcoefs[0] * t + xcoefs[1]) + xcoefs[2]) + xcoefs[3]
        y = t * (t * (ycoefs[0] * t + ycoefs[1]) + ycoefs[2]) + ycoefs[3]
        #x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        #y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]

        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t+= step


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
