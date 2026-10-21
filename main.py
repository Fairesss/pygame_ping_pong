import pygame as pg

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80

pg.init()


screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()
running = True

P1_position = [0, 0]
paddleP1 = pg.rect.Rect(*P1_position, PADDLE_WIDTH, PADDLE_HEIGHT)
P2_position = [WINDOW_WIDTH - PADDLE_WIDTH, 0]
paddleP2 = pg.rect.Rect(*P2_position, PADDLE_WIDTH, PADDLE_HEIGHT)



while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        paddleP1.move_ip(0, -1)
    if keys[pg.K_s]:
        paddleP1.move_ip(0, 1)

    if keys[pg.K_UP]:
        paddleP2.move_ip(0, -1)
    if keys[pg.K_DOWN]:
        paddleP2.move_ip(0, 1)

    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (255, 0, 0), paddleP1)
    pg.draw.rect(screen, (255, 0, 0), paddleP2)
    pg.display.flip()
    clock.tick(60)

pg.quit()
