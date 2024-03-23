import pygame
import math
import random

from shapes import I, O, T, S, Z, J, L, shapes, shape_colors, CYAN, YELLOW, PURPLE, GREEN, RED, BLUE, ORANGE, Piece

from pygame.locals import (
    QUIT,
    K_ESCAPE,
    K_DOWN,
    K_s,
    K_UP,
    K_w,
    K_LEFT,
    K_a,
    K_RIGHT,
    K_d
)


def draw_piece(piece):
    for i in range(len(piece.shape[piece.rotation][0])):
        for j in range(len(piece.shape[piece.rotation])):
            if piece.shape[piece.rotation][j][i] == '0':
                pygame.draw.rect(game, piece.color,
                                 grid_coordinates[j + piece.y][i + piece.x] + (BOX_SIZE, BOX_SIZE))


def is_position_valid(piece):
    for i in range(len(piece.shape[piece.rotation][0])):
        for j in range(len(piece.shape[piece.rotation])):
            if piece.shape[piece.rotation][j][i] == '0':
                if (piece.x + i) not in range(10) or (piece.y + j) not in range(20):
                    return False
    return True


def is_piece_at_bottom(piece):
    for i in range(len(piece.shape[piece.rotation][0])):
        for j in range(len(piece.shape[piece.rotation])):
            if piece.shape[piece.rotation][j][i] == '0' and piece.y + j == 19:
                return True
    return False

BOX_SIZE = 30
LINE_WIDTH = 2
BOUNDARY_WIDTH = 4
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
GAME_HEIGHT = 19 * LINE_WIDTH + 20 * BOX_SIZE
GAME_WIDTH = 9 * LINE_WIDTH + 10 * BOX_SIZE
OFFSET_HEIGHT = math.floor(0.9 * (WINDOW_HEIGHT - GAME_HEIGHT))
OFFSET_WIDTH = math.floor((WINDOW_WIDTH - GAME_WIDTH) / 2)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (120, 120, 120)

grid = [[0 for x in range(10)] for y in range(20)]

grid_coordinates = []
for y in range(20):
    grid_coordinates.append([])
    for x in range(10):
        grid_coordinates[y].append((x * (BOX_SIZE + LINE_WIDTH), y * (BOX_SIZE + LINE_WIDTH)))

confirmed_pieces = grid

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
game = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))

fall_clock = pygame.time.Clock()

fall_time = 0
fall_speed = 500

current_piece = Piece(3, 0, shapes[random.randint(0, len(shapes) - 1)])
create_new_piece = False

running = True
screen.fill(BLACK)

# draw border
pygame.draw.rect(screen, WHITE, (
    OFFSET_WIDTH - BOUNDARY_WIDTH, OFFSET_HEIGHT - BOUNDARY_WIDTH, GAME_WIDTH + 2 * BOUNDARY_WIDTH,
    GAME_HEIGHT + 2 * BOUNDARY_WIDTH), BOUNDARY_WIDTH)

while running:
    game.fill(BLACK)

    # draw gridlines
    for x in range(9):
        pygame.draw.line(game, GREY, (30 + 32 * x, 0), (30 + 32 * x, GAME_HEIGHT), LINE_WIDTH)

    for y in range(19):
        pygame.draw.line(game, GREY, (0, 30 + 32 * y), (GAME_WIDTH, 30 + 32 * y), LINE_WIDTH)

    if create_new_piece:
        new_piece = Piece(3, 0, shapes[random.randint(0, len(shapes) - 1)])
        create_new_piece = False
        current_piece = new_piece
    else:
        current_piece = current_piece

    if is_piece_at_bottom(current_piece):
        pygame.time.delay(1000)
        create_new_piece = True

    fall_time += fall_clock.get_rawtime()
    fall_clock.tick()

    if fall_time > fall_speed:
        fall_time = 0
        current_piece.y += 1
        if not is_position_valid(current_piece):
            current_piece.y -= 1

    draw_piece(current_piece)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == (K_s or K_DOWN):
                current_piece.y += 1
                if not is_position_valid(current_piece):
                    current_piece.y -= 1
            elif event.key == (K_d or K_RIGHT):
                current_piece.x += 1
                if not is_position_valid(current_piece):
                    current_piece.x -= 1
            elif event.key == (K_a or K_LEFT):
                current_piece.x -= 1
                if not is_position_valid(current_piece):
                    current_piece.x += 1
            # elif event.key == (K_w or K_UP):
            # rotate

    screen.blit(game, (OFFSET_WIDTH, OFFSET_HEIGHT))

    pygame.display.update()
