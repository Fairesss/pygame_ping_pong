import pygame as pg


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80
PADDLE_SPEED = 5

BALL_RADIUS = 20
BALL_SPEED = 5


def move_paddle(paddle: pg.Rect, speed: int):
    if paddle.y < 0:
        paddle.y = 0
    elif paddle.y > WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle.y = WINDOW_HEIGHT - PADDLE_HEIGHT
    else:
        paddle.move_ip(0, speed)

def move_ball(ball_position: pg.Vector2, current_direction: pg.Vector2,  speed: int):
    direction = pg.Vector2(0, 0)
    if ball_position.x < 0 + BALL_RADIUS:
        direction.x = 1
    elif ball_position.x > WINDOW_WIDTH - BALL_RADIUS:
        direction.x = -1
    else:
        direction.x = current_direction.x

    if ball_position.y < 0 + BALL_RADIUS:
        direction.y = 1
    elif ball_position.y > WINDOW_HEIGHT - BALL_RADIUS:
        direction.y = -1
    else:
        direction.y = current_direction.y

    ball_position += direction * speed
    return direction

pg.init()


screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()
running = True

P1_position = pg.Vector2([0, WINDOW_HEIGHT/2 - PADDLE_HEIGHT])
paddleP1 = pg.rect.Rect(*P1_position, PADDLE_WIDTH, PADDLE_HEIGHT)

P2_position = pg.Vector2([WINDOW_WIDTH - PADDLE_WIDTH, WINDOW_HEIGHT/2 - PADDLE_HEIGHT])
paddleP2 = pg.rect.Rect(*P2_position, PADDLE_WIDTH, PADDLE_HEIGHT)

ball_position = pg.Vector2([WINDOW_WIDTH//2, WINDOW_HEIGHT//2])
ball_direction = pg.Vector2(1, 0.5)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        move_paddle(paddleP1, -PADDLE_SPEED)
    if keys[pg.K_s]:
        move_paddle(paddleP1, PADDLE_SPEED)


    if keys[pg.K_UP]:
        move_paddle(paddleP2, -PADDLE_SPEED)
    if keys[pg.K_DOWN]:
        move_paddle(paddleP2, PADDLE_SPEED)

    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (255, 0, 0), paddleP1)
    pg.draw.rect(screen, (255, 0, 0), paddleP2)
    pg.draw.circle(screen, (255, 0, 0), ball_position, BALL_RADIUS)
    ball_direction = move_ball(ball_position, ball_direction, BALL_SPEED)

    pg.display.flip()
    clock.tick(60)

pg.quit()
