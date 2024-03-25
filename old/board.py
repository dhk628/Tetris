import pygame

grid = [[0 for x in range(10)] for y in range(20)]

grid_coordinates = []
for y in range(20):
    grid_coordinates.append([])
    for x in range(10):
        grid_coordinates[y].append((x * (BOX_SIZE + LINE_WIDTH), y * (BOX_SIZE + LINE_WIDTH)))

pygame.draw.rect(screen, WHITE, (
OFFSET_WIDTH - BOUNDARY_WIDTH, OFFSET_HEIGHT - BOUNDARY_WIDTH, GAME_WIDTH + 2 * BOUNDARY_WIDTH,
GAME_HEIGHT + 2 * BOUNDARY_WIDTH), BOUNDARY_WIDTH)

for x in range(9):
    pygame.draw.line(game, GREY, (30 + 32 * x, 0), (30 + 32 * x, GAME_HEIGHT), LINE_WIDTH)

for y in range(19):
    pygame.draw.line(game, GREY, (0, 30 + 32 * y), (GAME_WIDTH, 30 + 32 * y), LINE_WIDTH)

draw_shape(I, position, rotation)

screen.blit(game, (OFFSET_WIDTH, OFFSET_HEIGHT))

pygame.display.update()
