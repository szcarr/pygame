import pygame

import generation.worldgen as worldgen

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lol")

# Colors
WHITE = (255, 255, 255)
BLUE = (66, 221, 245)
PURPLE = (191, 66, 245)
BLACK = (0, 0, 0)

# Tile colors
MOUNTAINS = (105, 97, 120)
HILLS = (97, 54, 54)
GRASS = (46, 130, 48)
SHALLOW_WATER = (66, 221, 245)
DEEP_WATER = (28, 110, 232)

FPS = 60

GAMEHEIGHT = 32 + 16
GAMEWIDTH = 32 + 32

# Game tile size
TILESIZE = 30

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()

def main():
    run = True
    # GENERATE MAP
    clock = pygame.time.Clock()

    draw_window()

    my_rect = pygame.Rect(0, 0, 30, 30)

    worldmap = worldgen.generate(GAMEWIDTH, GAMEHEIGHT, 4)
    worldgen.printgeneration(worldmap, GAMEWIDTH, GAMEHEIGHT)
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): # <- add here
            if event.type == pygame.QUIT:
                run = False
            game_update(worldmap)

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
            if value > 85:
                color = MOUNTAINS
            elif value > 68:
                color = HILLS
            elif value > 40:
                color = GRASS
            elif value > 28:
                color = SHALLOW_WATER
            elif value > 0:
                color = DEEP_WATER
            pygame.draw.rect(WIN, color, pygame.Rect(TILESIZE * x, TILESIZE * y, TILESIZE, TILESIZE))
    pygame.display.flip()

if __name__ == "__main__":
    main()