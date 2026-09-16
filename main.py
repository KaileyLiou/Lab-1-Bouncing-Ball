import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Lab 1: Bouncing Ball")
clock = pygame.time.Clock() # tracks time and frame rate

x, y, dx, dy, r = 300, 200, 4, 3, 24 # initializing everything
gravity = 0.5 # pulls ball down 0.5 pixels per frame
friction = 0.85 # retains 85% of its speed after a bounce (loses 15%)
running = True

circle_color = (233, 30, 99)

# creating a circle class
class Circle:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.mass = r * r
        self.dx = random.randint(-4, 4)
        self.dy = random.randint(-4, 4)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # bounce from left and right walls
        if self.x - self.r <= 0 or self.x + self.r >= 600:
            self.dx *= -1

        # bounce from top and bottom walls
        if self.y - self.r <= 0 or self.y + self.r >= 400:
            self.dy *= -1

    def draw(self):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r
        )

circles = [] # list of random circles

for i in range(1000):
    x = random.randint(20, 580)
    y = random.randint(20, 380)
    r = random.randint(5, 15)

    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

    circle = Circle(x, y, r, color)
    circles.append(circle)

while running: # game loop
    for event in pygame.event.get(): # to get every single event
        if event.type == pygame.QUIT:
            running = False

    # dy += gravity # apply gravity
    # x += dx
    # y += dy

    # # horizontal bounce logic
    # if x - r < 0 or x + r > 600:
    #     dx = -dx
    #     circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # # vertical bounce logic
    # if y + r > 400:
    #     y = 400 - r
    #     dy = -dy * friction
    #     dx *= friction
    #     circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # elif y - r < 0:
    #     y = 0 + r
    #     dy = -dy * friction
    #     circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    for circle in circles:
        circle.move()

    # gravity and collisions between circles
    for i in range(len(circles)):
        for j in range(i + 1, len(circles)):

            c1 = circles[i]
            c2 = circles[j]

            dx = c2.x - c1.x
            dy = c2.y - c1.y

            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance == 0:
                continue

            # makes nearby circles pull toward each other
            force = 0.01 * c1.mass * c2.mass / (distance ** 2)

            fx = force * dx / distance
            fy = force * dy / distance

            c1.dx += fx / c1.mass
            c1.dy += fy / c1.mass

            c2.dx -= fx / c2.mass
            c2.dy -= fy / c2.mass

            # checks to see whether two circles are touching/overlapping
            if distance <= c1.r + c2.r:
                c1.dx, c2.dx = c2.dx, c1.dx
                c1.dy, c2.dy = c2.dy, c1.dy

    screen.fill((20, 24, 40))
    # pygame.draw.circle(screen, circle_color, (x,y), r)

    for circle in circles:
        circle.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()