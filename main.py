import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Lab 1: Bouncing Ball")
clock = pygame.time.Clock() # tracks time and frame rate

x, y, dx, dy, r = 300, 200, 4, 3, 24 # initializing everything
gravity = 0.5 # pulls ball down 0.5 pixels per frame
friction = 0.85 # retains 85% of its speed after a bounce (loses 15%)
running = True

circle_color = (233, 30, 99)

while running: # game loop
    for event in pygame.event.get(): # to get every single event
        if event.type == pygame.QUIT:
            running = False

    dy += gravity # apply gravity
    x += dx
    y += dy

    # horizontal bounce logic
    if x - r < 0 or x + r > 600:
        dx = -dx
        circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # vertical bounce logic
    if y + r > 400:
        y = 400 - r
        dy = -dy * friction
        dx *= friction
        circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    elif y - r < 0:
        y = 0 + r
        dy = -dy * friction
        circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.fill((20, 24, 40))
    pygame.draw.circle(screen, circle_color, (x,y), r)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
