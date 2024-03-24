import pygame
import math
import random
from time import sleep

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
    K_d,
    K_SPACE
)


def draw_piece(piece):
    for i in range(len(piece.shape[piece.rotation][0])):
        for j in range(len(piece.shape[piece.rotation])):
            if piece.shape[piece.rotation][j][i] == '0':
                pygame.draw.rect(game, piece.color,
                                 grid_coordinates[j + piece.y][i + piece.x] + (BOX_SIZE, BOX_SIZE))


def get_bottom_index(piece):
    for j in range(len(piece.shape[piece.rotation]) - 1, -1, -1):
        compare = piece.shape[piece.rotation][j]
        if compare != '.'*len(piece.shape[piece.rotation][0]):
            return j


def is_position_valid(piece, confirmed):
    for i in range(len(piece.shape[piece.rotation][0])):
        for j in range(len(piece.shape[piece.rotation])):
            if piece.shape[piece.rotation][j][i] == '0':
                if (piece.x + i) not in range(10) or (piece.y + j) not in range(20):
                    return False
                elif confirmed[piece.y + j][piece.x + i] != 0:
                    return False
    return True


def drop_piece(piece, confirmed):
    base = piece.y
    for j in range(20):
        dropped = piece
        dropped.y = base + j

        if not is_position_valid(dropped, confirmed):
            return j - 1


def is_piece_at_bottom(piece, confirmed):
    for i in range(len(piece.shape[piece.rotation][0])):
        for j in range(len(piece.shape[piece.rotation])):
            if piece.shape[piece.rotation][j][i] == '0' and piece.y + j == 19:
                return True
            elif piece.shape[piece.rotation][j][i] == '0' and piece.y + j + 1 < 20:
                if confirmed[piece.y + j + 1][piece.x + i] != 0:
                    return True
    return False


def confirm_piece(piece, confirmed):
    for i in range(len(piece.shape[piece.rotation][0])):
        for j in range(len(piece.shape[piece.rotation])):
            if piece.shape[piece.rotation][j][i] == '0':
                confirmed[piece.y + j][piece.x + i] = piece.color


def draw_confirmed(confirmed):
    for j in range(20):
        for i in range(10):
            if confirmed[j][i] == 0:
                pygame.draw.rect(game, BLACK, grid_coordinates[j][i] + (BOX_SIZE, BOX_SIZE))
            else:
                pygame.draw.rect(game, confirmed[j][i], grid_coordinates[j][i] + (BOX_SIZE, BOX_SIZE))


def check_completed_line(confirmed):
    for j in range(19, -1, -1):
        if 0 not in confirmed[j]:
            return j
    return -1


def is_game_over(piece, confirmed):
    for i in range(len(piece.shape[piece.rotation][0])):
        for j in range(len(piece.shape[piece.rotation])):
            if piece.shape[piece.rotation][j][i] == '0' and confirmed[piece.y + j][piece.x + i] != 0:
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

clock = pygame.time.Clock()
fall_clock = pygame.time.Clock()
held_clock = pygame.time.Clock()

fall_time = 0
fall_speed = 1000

held_time = 0
held_speed = 100

#current_piece = Piece(3, 0, shapes[random.randint(0, len(shapes) - 1)])
create_new_piece = True

running = True
game_over = False
screen.fill(BLACK)

# draw border
pygame.draw.rect(screen, WHITE, (
    OFFSET_WIDTH - BOUNDARY_WIDTH, OFFSET_HEIGHT - BOUNDARY_WIDTH, GAME_WIDTH + 2 * BOUNDARY_WIDTH,
    GAME_HEIGHT + 2 * BOUNDARY_WIDTH), BOUNDARY_WIDTH)

font = pygame.font.Font('freesansbold.ttf', 32)
game_over_text = font.render('Game Over', True, WHITE, BLACK)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (GAME_WIDTH // 2, GAME_HEIGHT // 2)

while running and not game_over:
    #clock.tick(10)

    dropped = False
    draw_confirmed(confirmed_pieces)

    # draw gridlines
    for x in range(9):
        pygame.draw.line(game, GREY, (30 + 32 * x, 0), (30 + 32 * x, GAME_HEIGHT), LINE_WIDTH)

    for y in range(19):
        pygame.draw.line(game, GREY, (0, 30 + 32 * y), (GAME_WIDTH, 30 + 32 * y), LINE_WIDTH)

    if create_new_piece:
        fall_time = 0
        new_piece = Piece(3, 0, shapes[random.randint(0, len(shapes) - 1)])
        if is_game_over(new_piece, confirmed_pieces):
            game_over = True
        else:
            draw_piece(new_piece)
            screen.blit(game, (OFFSET_WIDTH, OFFSET_HEIGHT))
            pygame.display.flip()
            pygame.event.clear()
            pygame.event.clear()
            create_new_piece = False
            current_piece = new_piece
            fall_clock.tick()
    else:
        current_piece = current_piece

    fall_time += fall_clock.get_rawtime()
    fall_clock.tick()

    if fall_time > fall_speed:
        fall_time = 0
        current_piece.y += 1
        if not is_position_valid(current_piece, confirmed_pieces):
            current_piece.y -= 1

    draw_piece(current_piece)

    keys = pygame.key.get_pressed()
    if keys[K_s] or keys[K_DOWN]:
        fall_time = 0
        held_time += held_clock.get_rawtime()
        held_clock.tick()
        if held_time > held_speed:
            fall_time = 0
            held_time = 0
            current_piece.y += 1
            if not is_position_valid(current_piece, confirmed_pieces):
                current_piece.y -= 1
    if keys[K_a] or keys[K_LEFT]:
        held_time += held_clock.get_rawtime()
        held_clock.tick()
        if held_time > held_speed:
            held_time = 0
            current_piece.x -= 1
            if not is_position_valid(current_piece, confirmed_pieces):
                current_piece.x += 1
    if keys[K_d] or keys[K_RIGHT]:
        held_time += held_clock.get_rawtime()
        held_clock.tick()
        if held_time > held_speed:
            held_time = 0
            current_piece.x += 1
            if not is_position_valid(current_piece, confirmed_pieces):
                current_piece.x -= 1

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            # elif event.key == (K_s or K_DOWN):
            #     current_piece.y += 1
            #     if not is_position_valid(current_piece, confirmed_pieces):
            #         current_piece.y -= 1
            #     else:
            #         fall_time = 0
            # elif event.key == (K_d or K_RIGHT):
            #     current_piece.x += 1
            #     if not is_position_valid(current_piece, confirmed_pieces):
            #         current_piece.x -= 1
            # elif event.key == (K_a or K_LEFT):
            #     current_piece.x -= 1
            #     if not is_position_valid(current_piece, confirmed_pieces):
            #         current_piece.x += 1
            elif event.key == (K_w or K_UP):
                current_piece.rotation = (current_piece.rotation + 1) % len(current_piece.shape)
                if not is_position_valid(current_piece, confirmed_pieces):
                    current_piece.rotation = (current_piece.rotation - 1) % len(current_piece.shape)
            elif event.key == K_SPACE:
                current_piece.y += drop_piece(current_piece, confirmed_pieces)
                confirm_piece(current_piece, confirmed_pieces)
                dropped = True
                create_new_piece = True
                draw_confirmed(confirmed_pieces)
                screen.blit(game, (OFFSET_WIDTH, OFFSET_HEIGHT))
                pygame.display.flip()
                pygame.event.pump()
                fall_time = 0
                fall_clock.tick()

    screen.blit(game, (OFFSET_WIDTH, OFFSET_HEIGHT))

    pygame.display.flip()

    if is_piece_at_bottom(current_piece, confirmed_pieces) and not dropped:
        create_new_piece = True
        confirm_piece(current_piece, confirmed_pieces)
        draw_confirmed(confirmed_pieces)
        screen.blit(game, (OFFSET_WIDTH, OFFSET_HEIGHT))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.wait(fall_speed)
        fall_time = 0
        fall_clock.tick()

    while check_completed_line(confirmed_pieces) != -1:
        del_row = check_completed_line(confirmed_pieces)
        confirmed_pieces[del_row] = [0]*10
        draw_confirmed(confirmed_pieces)
        screen.blit(game, (OFFSET_WIDTH, OFFSET_HEIGHT))
        pygame.display.flip()
        pygame.event.pump()
        #pygame.time.wait(fall_speed)
        for j in range(del_row - 1, -1, -1):
            confirmed_pieces[j + 1] = confirmed_pieces[j]
        draw_confirmed(confirmed_pieces)
        screen.blit(game, (OFFSET_WIDTH, OFFSET_HEIGHT))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.wait(held_speed)
        fall_time = 0
        fall_clock.tick()

while running and game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    #game.fill(BLACK)
    game.blit(game_over_text, game_over_rect)
    screen.blit(game, (OFFSET_WIDTH, OFFSET_HEIGHT))
    pygame.display.flip()
