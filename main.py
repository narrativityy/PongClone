# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

paddle_height = 200
paddle_width = 30

paddle_a_top = screen.get_height() / 2 - (paddle_height / 2)
paddle_a_left = 10

paddle_b_top = screen.get_height() / 2 - (paddle_height / 2)
paddle_b_left = screen.get_width() - paddle_width - 10


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.rect(screen, "green", (paddle_a_left, paddle_a_top, paddle_width, paddle_height), 0, 10)
    pygame.draw.rect(screen, 'red', (paddle_b_left, paddle_b_top, paddle_width, paddle_height), 0, 10)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_a_top -= 300 * dt
    if keys[pygame.K_s]:
        paddle_a_top += 300 * dt
    if keys[pygame.K_UP]:
        paddle_b_top -= 300 * dt
    if keys[pygame.K_DOWN]:
        paddle_b_top += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()