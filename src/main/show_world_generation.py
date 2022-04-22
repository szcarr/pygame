import pygame
import time

import generation.worldgen as worldgen
import generation.refineworld

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World generation showcase")

# Colors
WHITE = (255, 255, 255)
BLUE = (66, 221, 245)
PURPLE = (191, 66, 245)
BLACK = (0, 0, 0)

# Tile colors
BEACH = (214, 191, 88)
DEEP_WATER = (28, 110, 232)
GRASS = (46, 130, 48)
HILLS = (97, 54, 54)
SHALLOW_WATER = (66, 221, 245)
SNOW = (238, 237, 242)
MOUNTAINSBASE = (105, 97, 120)
MOUNTAINSHEAD = (76, 80, 87)

FPS = 60

GAMEHEIGHT = 16 * 6
GAMEWIDTH = 110

# Game tile size
TILESIZE = 6

GAMEHEIGHT = int(round(HEIGHT / TILESIZE)) + 1
GAMEWIDTH = int(round(WIDTH / TILESIZE)) + 1

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()

def main():
    run = True
    # GENERATE MAP
    clock = pygame.time.Clock()

    draw_window()

    #my_rect = pygame.Rect(0, 0, 30, 30)

    clock.tick(FPS)

    while True:
        worldmap = worldgen.primitive_generate(GAMEWIDTH, GAMEHEIGHT, 2, 1)
        worldgen.printgeneration(worldmap, GAMEWIDTH, GAMEHEIGHT)
        game_update(worldmap)

        length = 3
        for i in range(length):
            offset = 2
            if length - 1 == i:
                offset = 0
            worldmap = generation.refineworld.smooth_world(worldmap, GAMEWIDTH, GAMEHEIGHT, offset)
            worldgen.printgeneration(worldmap, GAMEWIDTH, GAMEHEIGHT)
            game_update(worldmap)

        WIN.fill(BLACK)
        time.sleep(20)
    pygame.quit()

def game_update(worldmap):
    object_update()
    background_update(worldmap)

def object_update():
    pass

def background_update(worldmap):
    # Creating tiles and assigning color based on their value
    for y in range(GAMEHEIGHT):
        for x in range(GAMEWIDTH):
            pos = f"{x} {y}"
            value = worldmap.get(pos)
            color = WHITE
            if value > 95:
                color = SNOW
            elif value > 89:
                color = MOUNTAINSHEAD
            elif value > 81:
                color = MOUNTAINSBASE
            elif value > 68:
                color = HILLS
            elif value > 40:
                color = GRASS
            elif value > 34:
                color = BEACH
            elif value > 24:
                color = SHALLOW_WATER
            elif value >= 0:
                color = DEEP_WATER
            pygame.draw.rect(WIN, color, pygame.Rect(TILESIZE * x, TILESIZE * y, TILESIZE, TILESIZE))
            pygame.display.flip()

if __name__ == "__main__":
    main()