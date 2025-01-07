import pygame

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
running = True
dt = 0
my_font = pygame.font.SysFont('Comic Sans MS', 30)

player1_score = 0
player2_score = 0

paddle_height = 200
paddle_width = 30

paddle_a_top = screen.get_height() / 2 - (paddle_height / 2)
paddle_a_left = 10

paddle_b_top = screen.get_height() / 2 - (paddle_height / 2)
paddle_b_left = screen.get_width() - paddle_width - 10

ball_pos_x = screen.get_width() / 2
ball_pos_y = screen.get_height() / 2

ball_speed = 300

ball_direction_x = 1
ball_direction_y = 1

single_player = False
single_player_button_color = "red"

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                single_player = not single_player
                if single_player:
                    single_player_button_color = "green"
                else:
                    single_player_button_color = "red"
                print(single_player)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    player1_score_text = my_font.render("Player 1: " + str(player1_score), True, "white")
    player2_score_text = my_font.render("Player 2: " + str(player2_score), True, "white")
    screen.blit(player1_score_text, (10, 10))
    screen.blit(player2_score_text, (screen.get_width() - player2_score_text.get_width() - 10, 10))

    pygame.draw.rect(screen, "green", (paddle_a_left, paddle_a_top, paddle_width, paddle_height), 0, 10)
    pygame.draw.rect(screen, 'red', (paddle_b_left, paddle_b_top, paddle_width, paddle_height), 0, 10)

    pygame.draw.circle(screen, "white", (ball_pos_x, ball_pos_y), 25)

    button_text = my_font.render("Single Player", True, single_player_button_color)
    screen.blit(button_text, (screen.get_width() - 10 - button_text.get_width(), screen.get_height() - 10 - button_text.get_height()))

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if ball_pos_y - 25 <= 0:
        ball_direction_y = 1
    if ball_pos_y + 25 >= screen.get_height():
        ball_direction_y = -1
    if ball_pos_x <= 10 + paddle_width + 25 and paddle_a_top <= ball_pos_y <= paddle_a_top + paddle_height:
        ball_direction_x = 1
    if ball_pos_x >= screen.get_width() - 10 - paddle_width - 25 and paddle_b_top <= ball_pos_y <= paddle_b_top + paddle_height:
        ball_direction_x = -1
    if ball_pos_x - 25 <= 0:
        player2_score += 1
        print(player2_score)
        ball_pos_x = screen.get_width() / 2
        ball_pos_y = screen.get_height() / 2
        ball_direction_x = 1
    if ball_pos_x + 25 >= screen.get_width():
        player1_score += 1
        print(player1_score)
        ball_pos_x = screen.get_width() / 2
        ball_pos_y = screen.get_height() / 2
        ball_direction_x = -1

    ball_pos_x += ball_speed * dt * ball_direction_x
    ball_pos_y += ball_speed * dt * ball_direction_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if paddle_a_top <= 0:
            paddle_a_top = 0
        else:
            paddle_a_top -= 300 * dt
    if keys[pygame.K_s]:
        if paddle_a_top >= screen.get_height() - paddle_height:
            paddle_a_top = screen.get_height() - paddle_height
        else:
            paddle_a_top += 300 * dt
    if not single_player:
        if keys[pygame.K_UP]:
            if paddle_b_top <= 0:
                paddle_b_top = 0
            else:
                paddle_b_top -= 300 * dt
        if keys[pygame.K_DOWN]:
            if paddle_b_top >= screen.get_height() - paddle_height:
                paddle_b_top = screen.get_height() - paddle_height
            else:
                paddle_b_top += 300 * dt
    else:
        if ball_pos_y < paddle_b_top + paddle_height / 2:
            if paddle_b_top <= 0:
                paddle_b_top = 0
            else:
                paddle_b_top -= 200 * dt
        if ball_pos_y > paddle_b_top + paddle_height / 2:
            if paddle_b_top >= screen.get_height() - paddle_height:
                paddle_b_top = screen.get_height() - paddle_height
            else:
                paddle_b_top += 200 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()