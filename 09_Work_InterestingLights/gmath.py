import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    amb = calculate_ambient(ambient, areflect)
    dif = calculate_diffuse(light, dreflect, normal)
    spe = calculate_specular(light, sreflect, view, normal)

    ret_val = []
    for each in range(3):
        ret_val.append(limit_color(int(amb[each] + dif[each] + spe[each])))
    return ret_val
    #pass

def calculate_ambient(alight, areflect):
    ret_val =  []
    for each in range(3):
        ret_val.append(areflect[each] * alight[each])
    return ret_val
    #pass

def calculate_diffuse(light, dreflect, normal):
    normalize(normal)
    normalize(light[LOCATION])
    ln = dot_product(normal, light[LOCATION])

    ret_val = []
    for each in range(3):
        some_num = 0
        some_num = light[COLOR][each] * dreflect[each]
        ret_val.append(some_num * ln)
    return ret_val
    #pass

def calculate_specular(light, sreflect, view, normal):
    normalize(light[LOCATION])
    normalize(view)
    normalize(normal)

    temp = dot_product(normal,light[LOCATION])
    some_val = []

    for each in range(3):
        x = 0
        x = (2 * (normal[each]) * temp) - light[LOCATION][each]
        some_val.append(x)

    retval = dot_product(some_val, view)
    if retval < 0:
        retval = 0

    ret_val = []
    for each in range(3):
        a = 0
        a = light[COLOR][each] * sreflect[each] * (retval ** SPECULAR_EXP)
        ret_val.append(a)
    return ret_val
    #pass

def limit_color(color):
    if color < 0:
        return 0
    elif color > 255:
        return 255
    else:
        return color
    #pass

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
