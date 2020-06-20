from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if(x0 > x1 ):
        temp = x0
        x0 = x1
        x1 = temp
        temp = y0
        y0 = y1
        y1 = temp

    if ((x0 - x1) == 0):
        while (y0 <= y1):
            plot(screen, color, x0, y0)
            y0 += 1
    else:

        x = x0
        y = y0
        A = y1 - y0
        B = -1 * (x1 - x0)
        m = A / (B * -1.0)

        #print(m)

        if (m <= 1 and m >= 0):
            d = 2 * A + B
            #print("Octant I / V")
            while (x <= x1):
                plot(screen, color, x, y)
                if (d > 0):
                    y += 1
                    d += 2 * B
                x += 1
                d += 2 * A

        if (m > 1):
            d = A + 2 * B
            #print("Octant II")
            while (y <= y1):
                plot(screen, color, x, y)
                if (d < 0):
                    x += 1
                    d += 2 * A
                y += 1
                d += 2 * B

        if (m <= -1):
            d = 2 * A + B
            #print("Octant III")
            while (y >= y1):
                #print ("[" + str(x) + "," + str(y) + "]")
                plot(screen, color, x, y)
                if (d > 0):
                    x += 1
                    d += 2 * A
                y -= 1
                d -= 2 * B

        if (m <= 0 and m > -1):
            d = A + 2 * B
            #print("Octant IV")
            while (x <= x1):
                #print ("[" + str(x) + "," + str(y) + "]")
                plot(screen, color, x, y)
                if (d < 0):
                    y -= 1
                    d -= 2 * B
                x += 1
                d += 2 * A

    #pass
