import pygame
import sys

pygame.init()

# User input
speed = int(input("Enter movement speed: "))
fps = int(input("Enter FPS: "))
radius = int(input("Enter circle size: "))

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Custom Circle with Axes")

x, y = width // 2, height // 2

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

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

    # Keep inside screen
    x = max(radius, min(width - radius, x))
    y = max(radius, min(height - radius, y))

    screen.fill((240, 240, 240))

    # Draw axes
    pygame.draw.line(screen, (0, 0, 0), (0, height//2), (width, height//2), 2)
    pygame.draw.line(screen, (0, 0, 0), (width//2, 0), (width//2, height), 2)

    # Draw circle
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    # Show coordinates relative to center
    coord_text = f"X: {x - width//2}, Y: {height//2 - y}"
    text = font.render(coord_text, True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(fps)