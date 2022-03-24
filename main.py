from mandelbrot import isMandelbrot, Complex, iterations
import pygame
import sys

WIDTH = 300
HEIGHT = 200
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

ZOOM = 0.3

WIDTH_SCALE = ZOOM / WIDTH
HEIGHT_SCALE = ZOOM / HEIGHT

LEFT = 1.2

# Draw the mandelbrot set
for x in range(WIDTH):
    for y in range(HEIGHT):
        result = isMandelbrot(Complex(x * WIDTH_SCALE - (ZOOM * 5 / 8 + LEFT), y * WIDTH_SCALE - (ZOOM/2 + 0.21) * HEIGHT/WIDTH))

        # the bigger the number, the more time it takes to go to infinity
        # so the darker the colour

        if result == True:
            colour = (0, 0, 0)
        else:
            colour = ((result / iterations * 255), (result / iterations * 255), 255)
        
        SCREEN.set_at((x, y), colour)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()