import pygame
import sys

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Circle with Axes")

x, y = width // 2, height // 2
radius = 20
speed = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill((255, 255, 255))

    pygame.draw.line(screen, (0, 0, 0), (0, height//2), (width, height//2), 2)  # X-axis
    pygame.draw.line(screen, (0, 0, 0), (width//2, 0), (width//2, height), 2)  # Y-axis

    # Draw circle
    pygame.draw.circle(screen, (0, 0, 255), (x, y), radius)

    pygame.display.update()
    clock.tick(60)