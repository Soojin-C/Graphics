from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

# draw_line( 0, 0, 500, 100, screen, color )
# #draw_line( 0, 0, 100, 500, screen, color )
# draw_line( 100, 500, 0, 0, screen, color )
# draw_line( 500, 0, 400, 500, screen, color )
#draw_line( 500, 0, 0, 100, screen, color )
#
# draw_line( 0, 400, 500, 500, screen, color )
# draw_line( 400, 0, 500, 500, screen, color )
# draw_line( 0, 250, 500, 250, screen, color )
#
# draw_line( 250, 0, 250, 500, screen, color )
#
# draw_line( 0, 0, 500, 500, screen, color )
# draw_line( 500, 500, 0, 0, screen, color )
#
# draw_line( 0, 0, 500, 100, screen, color )
# draw_line( 0, 0, 500, 100, screen, color )

# draw_line( 0, 500, 0, 0, screen, color )
# draw_line( 0, 499, 250, 0, screen, color )

x = 0
y = 500
x1 = 0
y1 = 0

while (x1 <= 500):
    draw_line(x, y, x1, y1, screen, color)
    color[2] += 5
    draw_line(x1, y1, 500 - x1, 500, screen, color)

    y -= 10
    x1 += 10

x = 0
y = 500
x1 = 500
y1 = 500
color = [0, 0, 255]

while (x <= 500):
    draw_line(x, y, x1, y1, screen, color)
    draw_line(x1, y1, 0, 500 - y1, screen, color)
    color[0] += 5
    y1 -= 10
    x += 10

print("--> img.png")


display(screen)
save_extension(screen, 'img.png')
