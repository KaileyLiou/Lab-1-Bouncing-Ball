import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My first pygame!")
clock = pygame.time.Clock() # tracks time and frame rate

x, y, dx, dy, r = 300, 200, 4, 3, 24 # initializing everything
running = True

while running: # game loop
    for event in pygame.event.get(): # to get every single event
        if event.type == pygame.QUIT:
            running = False

    x += dx
    y += dy
    
    if x - r < 0 or x + r > 600:
        dx = -dx

    if y - r < 0 or y + r > 400:
        dy = -dy

    screen.fill((20, 24, 40))
    pygame.draw.circle(screen, (233, 30, 99), (x,y), r)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
