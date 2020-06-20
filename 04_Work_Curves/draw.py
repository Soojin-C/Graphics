from display import *
from matrix import *

#add_edge( matrix, x0, y0, z0, x1, y1, z1 )

def add_circle( points, cx, cy, cz, r, step ):

    alpha = 2*math.pi * step

    x = cx + (r * math.cos(0))
    y = cy + (r * math.sin(0))

    t = 0
    while t <= 2*math.pi:
        x2 = cx + (r * math.cos(t))
        y2 = cy + (r * math.sin(t))
        #print(x2, y2)
        add_edge(points, x, y, 0, x2, y2, 0)

        x = x2
        y = y2
        t += alpha
    #pass

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    t = 0
    x = x0
    y = y0

    if curve_type == 'hermite':
        coef1 = generate_curve_coefs(x0, x1, x1, x3, [x2, x3])[0]
        coef2 = generate_curve_coefs(y0, y1, y1, y2, [y2, y3])[0]
        print(coef1,0,coef2)
    else:
        coef1 = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
        coef2 = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    while t <= 1:
        x = helper2(coef1[0], t, 3) + helper2(coef1[1], t, 2) + helper2(coef1[2], t, 1) + helper2(coef1[3], t, 0)
        y = helper2(coef2[0], t, 3) + helper2(coef2[1], t, 2) + helper2(coef2[2], t, 1) + helper2(coef2[3], t, 0)
        print(x,y)

        t = t + step
        print("--------")

        xend = helper2(coef1[0], t, 3) + helper2(coef1[1], t, 2) + helper2(coef1[2], t, 1) + helper2(coef1[3], t, 0)
        yend = helper2(coef2[0], t, 3) + helper2(coef2[1], t, 2) + helper2(coef2[2], t, 1) + helper2(coef2[3], t, 0)

        print(xend, yend)

        add_edge(points, x, y, 0, xend, yend, 0)


    #pass
def cube( val, pow):
    return math.pow(val, pow)
def helper2( val2 , val, pow):
    return val2 * cube(val, pow)


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print ('Need at least 2 points to draw')
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
