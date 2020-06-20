img = open("img.ppm", "w")
img.write("P3 \n500 500 \n255\n")

row = 0
while (row < 500):
    column = 0
    while (column < 255):
        img.write(str(column) + " 0 " + str(row) + " ")
        column = column + 1
    while (column > 0):
        img.write(str(column) + " 0 " + str(row) + " ")
        column = column - 1
    row = row + 1


img.close()
