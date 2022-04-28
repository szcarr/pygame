import pygame
import time

import generation.worldgen
import generation.refineworld
import generation.circumference.circumference as circumference
import seeds

import tiles.tiles as tiles

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 900
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("World generation showcase")

FPS = 60

# Game tile size
TILESIZE = 80 # was 6


GAMEHEIGHT = int(round(WINDOW_HEIGHT / TILESIZE)) + 1
GAMEWIDTH = int(round(WINDOW_WIDTH / TILESIZE)) + 1

print(GAMEHEIGHT * GAMEWIDTH)

tilelist = tiles.load_TileTypes() # All different tiles

def draw_window():
    WIN.fill((255, 255, 255))
    pygame.display.update()

def main(**kwargs):
    clock = pygame.time.Clock()

    draw_window()

    clock.tick(FPS)
    
    tiles.print_loaded_tiles()

    # Settings
    seed = None
    for k in kwargs:
        if k == "Seed":
            seed = kwargs.get(k)


    while True:
        if seed:
            print("Loading from seed")
            updated_worldmap = seeds.load_from_seed(seed)
            worldmap = {}
            game_update(worldmap, updated_worldmap)
            worldmap = updated_worldmap
            
            updated_worldmap = circumference.get_circumference(tiles.get_tile_by_name(tilelist, "Deep water").tile_id, "2 5", worldmap)
            game_update(worldmap, updated_worldmap)
            worldmap = updated_worldmap

        else: # Not loading from seed then defaults to random world gen
            #ADDING PLAINS
            worldmap = generation.worldgen.generate_plains(GAMEWIDTH, GAMEHEIGHT, tilelist)
            updated_worldmap = worldmap
            game_update(worldmap, updated_worldmap)

            #Adding ocean
            ocean_generate_pos =  f"{int(round(GAMEWIDTH / 2)) + 1} {int(round(GAMEHEIGHT / 2)) + 1}"
            size = (GAMEHEIGHT * GAMEWIDTH) * 0.0221
            updated_worldmap = generation.worldgen.generate_ocean(size, 9, worldmap, ocean_generate_pos, tilelist)
            game_update(worldmap, updated_worldmap)
            worldmap = updated_worldmap

            #print("STARTING SMOOTGING")
            updated_worldmap = generation.refineworld.smooth_world(worldmap, GAMEWIDTH, GAMEHEIGHT, 0, True)
            game_update(worldmap, updated_worldmap)
            worldmap = updated_worldmap
            print("FINISHED SMOOTGING")

            #Circumference
            print("CIRCUMFRENRECE")
            start_p = circumference.get_furthest_value(tiles.get_tile_by_name(tilelist, "Deep water").tile_id, ocean_generate_pos, worldmap)
            updated_worldmap = circumference.get_circumference(tiles.get_tile_by_name(tilelist, "Deep water").tile_id, start_p, worldmap)

            game_update(worldmap, updated_worldmap)

            worldmap = updated_worldmap
            
            length = 0 # <- is 3
            for i in range(length):
                offset = 2
                if length - 1 == i:
                    offset = 0
                worldmap = generation.refineworld.smooth_world(worldmap, GAMEWIDTH, GAMEHEIGHT, offset)
                game_update(worldmap)

        WIN.fill((0, 0, 0))
        time.sleep(5)
    pygame.quit()

def game_update(worldmap, updated_worldmap):
    object_update()
    background_update(worldmap, updated_worldmap)

def object_update():
    pass

def background_update(worldmap, updated_worldmap):
    # Creating tiles and assigning color based on their value
    for y in range(GAMEHEIGHT):
        for x in range(GAMEWIDTH):
            pos = f"{x} {y}"
            value = worldmap.get(pos)
            updated_value = updated_worldmap.get(pos)
            if value == -1:
                '''
                -1 Means the tile should keep its previous color
                '''
                continue
            elif value == updated_value:
                '''
                Does not need to update a value that has the same value
                '''
                continue
            tile = tiles.get_tile_by_id(tilelist, updated_value)
            if tile != None:
                color = tile.color
                pygame.draw.rect(WIN, color, pygame.Rect(TILESIZE * x, TILESIZE * y, TILESIZE, TILESIZE))
                pygame.display.flip()

if __name__ == "__main__":
    main(Seed = "/home/scp092/Documents/pygame/src/seeds/water.txt")