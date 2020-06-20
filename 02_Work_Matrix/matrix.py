"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1   1       1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    counter = 0
    retVal = ""
    while (counter < 4):
        for each in matrix:
            retVal += str(each[counter]) + "\t"
        counter += 1
        print(retVal)
        retVal = ""
    # pass

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    row = 0
    col = 0
    for each in matrix:
        for num in each:
            if (row == col):
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0
            col += 1
        col = 0
        row += 1
    # pass

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    tempM = new_matrix(len(m2[0]),len(m2))
    for row in range (len(m2[0])):
        for col in range(len(m2)):
            result = 0
            for each in range(len(m1)):
                result += (m1[each][row] * m2[col][each])
            tempM[col][row] = result

    for each in range (len(m2[0])):
        for curr in range(len(m2)):
            m2[curr][each] = tempM[curr][each]
    return m2
    #pass


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
