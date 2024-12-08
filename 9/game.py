from math import nan, sqrt
import pygame
import random
import sys


BALL_INITIAL_SPEED = 100
BALL_ACCELERATION = 10.0
BALL_RADIUS = 12

PADDLE_WIDTH = 16
PADDLE_HEIGHT = 128
PADDLE_SPEED = 200.0
PADDLE_AUTO_SPEED = {
    "human": 0.0,
    "easy": 150.0,
    "medium": 250.0,
    "hard": 500.0,
}

POINT_GOAL = 11

SNOW_SIZE = 64
SNOW_SPEED = 100.0
SNOW_ADD_EVENT = pygame.event.custom_type()
SNOW_SPAWN_TIME = {
    "human": 2000,
    "easy": 5000,
    "medium": 2000,
    "hard": 1000,
}

MARGIN = 16

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def center(offset=(0, 0)):
    size = pygame.display.get_window_size()
    return size[0] // 2 - offset[0] // 2, size[1] // 2 - offset[1] // 2


def clamp(val, min, max):
    if val < min:
        return min
    elif val > max:
        return max
    else:
        return val


def sign(n):
    if n == 0.0:
        return 0.0
    elif n > 0.0:
        return 1.0
    elif n < 0.0:
        return -1.0
    else:
        return nan


def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720), vsync=1)
pygame.display.set_caption("Pong")

difficulty = next(
    filter(lambda a: a in ["easy", "medium", "hard"], sys.argv[1::]), "human"
)
snow = [] if "snow" in sys.argv[1::] else None
if snow is not None:
    pygame.time.set_timer(SNOW_ADD_EVENT, SNOW_SPAWN_TIME[difficulty])
snow_icon = pygame.image.load("./snow.png")
font = pygame.font.SysFont(None, 32)
clock = pygame.time.Clock()


state = "start"
points = [0, 0]

left_paddle_y = center()[1]
right_paddle_y = center()[1]

ball_x = center()[0]
ball_y = center()[1]
ball_vx = float(BALL_INITIAL_SPEED)
ball_vy = float(
    random.randint(
        -BALL_INITIAL_SPEED // 2,
        BALL_INITIAL_SPEED // 2,
    )
)

dt = 0.0


while True:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                sys.exit()
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_SPACE if state != "playing":
                        snow = [] if snow is not None else None
                        points = [0, 0]
                        left_paddle_y = center()[1]
                        right_paddle_y = center()[1]
                        ball_x = center()[0]
                        ball_y = center()[1]
                        ball_vx = float(BALL_INITIAL_SPEED)
                        ball_vy = float(
                            random.randint(
                                -BALL_INITIAL_SPEED,
                                BALL_INITIAL_SPEED,
                            )
                        )
                        state = "playing"
                    case pygame.K_ESCAPE if state != "playing":
                        sys.exit()
                    case pygame.K_ESCAPE:
                        state = "end"
            case (
                pygame.MOUSEBUTTONDOWN
            ) if event.button == 1 and snow is not None:
                clicked = []
                for i, flake in enumerate(snow):
                    if dist(flake, event.pos) <= SNOW_SIZE / 2:
                        clicked.append(i)

                for i in reversed(clicked):
                    snow.pop(i)
            case event if event == SNOW_ADD_EVENT:
                snow.append(
                    [
                        float(
                            random.randint(
                                MARGIN + PADDLE_WIDTH + SNOW_SIZE,
                                pygame.display.get_window_size()[0]
                                - (MARGIN + PADDLE_WIDTH + SNOW_SIZE),
                            )
                        ),
                        0,
                    ]
                )

    right_paddle_y += (
        sign(ball_y - right_paddle_y) * PADDLE_AUTO_SPEED[difficulty] * dt
    )

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle_y -= PADDLE_SPEED * dt
    if keys[pygame.K_s]:
        left_paddle_y += PADDLE_SPEED * dt
    if keys[pygame.K_i] and difficulty == "human":
        right_paddle_y -= PADDLE_SPEED * dt
    if keys[pygame.K_k] and difficulty == "human":
        right_paddle_y += PADDLE_SPEED * dt

    ball_x += ball_vx * dt
    ball_y += ball_vy * dt
    ball_vx = sign(ball_vx) * (abs(ball_vx) + BALL_ACCELERATION * dt)
    ball_vy = sign(ball_vy) * (abs(ball_vy) + BALL_ACCELERATION * dt)

    if (
        ball_y < BALL_RADIUS
        or ball_y > pygame.display.get_window_size()[1] - BALL_RADIUS
    ):
        ball_vy = -ball_vy
        ball_y = clamp(
            ball_y,
            BALL_RADIUS,
            pygame.display.get_window_size()[1] - BALL_RADIUS,
        )

    if ball_x < BALL_RADIUS:
        points[1] += 1

        ball_x = center()[0]
        ball_y = center()[1]
        snow = [] if snow is not None else None
        ball_vx = float(BALL_INITIAL_SPEED)
        ball_vy = float(
            random.randint(
                -BALL_INITIAL_SPEED // 2,
                BALL_INITIAL_SPEED // 2,
            )
        )
    elif ball_x > pygame.display.get_window_size()[0] - BALL_RADIUS:
        points[0] += 1

        ball_x = center()[0]
        ball_y = center()[1]
        snow = [] if snow is not None else None
        ball_vx = float(BALL_INITIAL_SPEED)
        ball_vy = float(
            random.randint(
                -BALL_INITIAL_SPEED // 2,
                BALL_INITIAL_SPEED // 2,
            )
        )
    elif (
        ball_x < MARGIN + PADDLE_WIDTH + BALL_RADIUS
        and left_paddle_y - PADDLE_HEIGHT / 2
        < ball_y
        < left_paddle_y + PADDLE_HEIGHT / 2
    ):
        ball_vx = -ball_vx
        ball_x = MARGIN + PADDLE_WIDTH + BALL_RADIUS
    elif (
        ball_x
        > pygame.display.get_window_size()[0]
        - (MARGIN + PADDLE_WIDTH + BALL_RADIUS)
        and right_paddle_y - PADDLE_HEIGHT / 2
        < ball_y
        < right_paddle_y + PADDLE_HEIGHT / 2
    ):
        ball_vx = -ball_vx
        ball_x = pygame.display.get_window_size()[0] - (
            MARGIN + PADDLE_WIDTH + BALL_RADIUS
        )

    to_remove = []
    for i, flake in enumerate(snow if snow is not None else []):
        flake[1] += SNOW_SPEED * dt
        if flake[1] > pygame.display.get_window_size()[1]:
            to_remove.append(i)
            points[int(ball_vx > 0)] = max(points[int(ball_vx > 0)] - 1, 0)

    for i in reversed(to_remove):
        snow.pop(i)

    match state:
        case "start":
            text = font.render("Press [space] to start.", True, WHITE)
            screen.blit(text, center(text.get_size()))
        case "playing":
            screen.blits(
                map(
                    lambda flake: (
                        snow_icon,
                        (flake[0] - SNOW_SIZE // 2, flake[1] - SNOW_SIZE // 2),
                    ),
                    snow if snow is not None else [],
                ),
                0,
            )

            pygame.draw.rect(
                screen,
                WHITE,
                pygame.Rect(
                    MARGIN,
                    left_paddle_y - PADDLE_HEIGHT / 2,
                    PADDLE_WIDTH,
                    PADDLE_HEIGHT,
                ),
            )

            pygame.draw.rect(
                screen,
                WHITE,
                pygame.Rect(
                    pygame.display.get_window_size()[0] - PADDLE_WIDTH - MARGIN,
                    right_paddle_y - PADDLE_HEIGHT / 2,
                    PADDLE_WIDTH,
                    PADDLE_HEIGHT,
                ),
            )

            pygame.draw.circle(
                screen,
                WHITE,
                (ball_x, ball_y),
                BALL_RADIUS,
            )

            left_paddle_y = clamp(
                left_paddle_y,
                PADDLE_HEIGHT / 2,
                pygame.display.get_window_size()[1] - PADDLE_HEIGHT / 2,
            )

            right_paddle_y = clamp(
                right_paddle_y,
                PADDLE_HEIGHT / 2,
                pygame.display.get_window_size()[1] - PADDLE_HEIGHT / 2,
            )

            text = font.render(f"{points[0]} : {points[1]}", True, WHITE)
            screen.blit(
                text,
                center(
                    (
                        text.get_size()[0],
                        pygame.display.get_window_size()[1] - 2 * MARGIN,
                    )
                ),
            )
        case "end":
            text = font.render(
                f"{'Left' if points[0] > points[1] else 'Right' if points[0] < points[1] else 'No'} player won!",
                True,
                WHITE,
            )
            screen.blit(text, center((text.get_size()[0], 32)))

            text = font.render(
                "Press [space] to play again.",
                True,
                WHITE,
            )
            screen.blit(text, center((text.get_size()[0], -32)))

    if any(map(lambda p: p >= POINT_GOAL, points)):
        state = "end"

    pygame.display.flip()
    screen.fill(BLACK)
    dt = clock.tick() / 1000
