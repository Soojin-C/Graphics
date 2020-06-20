from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print("Testing identity matrix: ")
ident(matrix)
print_matrix(matrix)
print("= = = = = = = = = = = = = = = = =")

print("Testing add_edge: ")
matrix2 = []
add_edge(matrix2, 1, 2, 3, 4, 5, 6)
print_matrix(matrix2)
print("= = = = = = = = = = = = = = = = =")

print("Testing matrix_mult: matrix * matrix2")
matrix_mult(matrix, matrix2)
print_matrix(matrix2)
print("and matrix3 * new matrix2")
matrix3 = []
add_edge(matrix3, 1, 2, 3, 4, 5, 6)
add_edge(matrix3, 7, 8, 9, 10, 11, 12)
matrix_mult(matrix3, matrix2)
print_matrix(matrix2)
print("= = = = = = = = = = = = = = = = =")

color = [ 179, 224, 255 ]
matrix = []

x = 0
y = 0
X = 500
Y = 0

while (y <= 250):
    add_edge(matrix, y, 0, 0, 500, y, 0)
    add_edge(matrix, x, y, 0, X, Y, 0)
    add_edge(matrix, y, 500, 0, x, y, 0)
    add_edge(matrix, y, 500, 0, 500, X, 0)
    y += 5
    X -= 5


draw_lines( matrix, screen, color )
display(screen)
save_extension(screen, "pic.png")
print("==> pic.png")
