import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    helper = dot_product(vector, vector)
    val = math.sqrt(helper)

    vector[0] = x / val
    vector[1] = y / val
    vector[2] = z / val

    #pass

#Return the dot porduct of a . b
def dot_product(a, b):
    val0 = a[0] * b[0]
    val1 = a[1] * b[1]
    val2 = a[2] * b[2]
    return val0 + val1 + val2

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    first = polygons[i]
    second = polygons[i + 1]
    third = polygons[i + 2]

    a = [second[0] - first[0], second[1] - first[1], second[2] - first[2]]
    b = [third[0] - first[0], third[1] - first[1], third[2] - first[2]]

    normal = [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]

    return normal
