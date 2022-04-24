import pygame
import time

import generation.worldgen
import generation.refineworld
import tiles.tiles as tiles

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World generation showcase")

# Colors
WHITE = (255, 255, 255)
BLUE = (66, 221, 245)
PURPLE = (191, 66, 245)
BLACK = (0, 0, 0)

FPS = 60

GAMEHEIGHT = 16 * 6
GAMEWIDTH = 110

# Game tile size
TILESIZE = 6

GAMEHEIGHT = int(round(HEIGHT / TILESIZE)) + 1
GAMEWIDTH = int(round(WIDTH / TILESIZE)) + 1

tilelist = tiles.load_TileTypes() # All different tiles

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    draw_window()

    clock.tick(FPS)
    
    while True:
        #ADDING PLAINS
        worldmap = generation.worldgen.generate_plains(GAMEWIDTH, GAMEHEIGHT, tilelist)
        #generation.worldgen.printgeneration(worldmap, GAMEWIDTH, GAMEHEIGHT)
        game_update(worldmap)

        #Adding ocean        
        worldmap = generation.worldgen.generate_ocean(500, 9, worldmap, f"{int(round(GAMEWIDTH / 2)) + 1} {int(round(GAMEHEIGHT / 2)) + 1}", tilelist)
        game_update(worldmap)


        length = 0 # <- is 3
        for i in range(length):
            offset = 2
            if length - 1 == i:
                offset = 0
            worldmap = generation.refineworld.smooth_world(worldmap, GAMEWIDTH, GAMEHEIGHT, offset)
            game_update(worldmap)

        WIN.fill(BLACK)
        time.sleep(5)
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
            if value == -1:
                '''
                -1 Means the tile should keep its previous color
                '''
                continue 
            tile = tiles.get_tile_by_id(tilelist, value)
            if tile != None:
                color = tile.color
                pygame.draw.rect(WIN, color, pygame.Rect(TILESIZE * x, TILESIZE * y, TILESIZE, TILESIZE))
                pygame.display.flip()

if __name__ == "__main__":
    main()