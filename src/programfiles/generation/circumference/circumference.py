import pygame
import time

import show_world_generation

def get_circumference(target_value, start_coordinates, world_map):

    '''
    target_value is the value you want to get the circumference from.
    '''

    outline = draw_outline(target_value, start_coordinates, world_map)
    return outline

def get_furthest_value(target_value, start_coordinates, world_map) -> str:

    '''
    Going west
    '''

    counter = 0
    stop_count = 0
    furthest_pos = ""
    while True:
        if stop_count == 3:
            print("FURTH", furthest_pos)
            furthest_pos = f'{int(furthest_pos.split(" ")[0]) - 1} {int(furthest_pos.split(" ")[1])}'
            break
        x, y = int(start_coordinates.split(" ")[0]), int(start_coordinates.split(" ")[1])
        current_pos = f"{x - counter} {y}"
        current_value = world_map.get(current_pos)
        print(current_pos, current_value, target_value)
        if current_value == target_value:
            furthest_pos = current_pos
        else:
            stop_count += 1
        counter += 1
    return furthest_pos

def draw_outline(target_value, start_coordinates, world_map) -> dict:
    OFFSET = [
        "-1 -1", "0 -1", "1 -1",
        "-1 0", "0 0", "1 0",
        "-1 1", "0 1", "1 1",
    ]

    current_pos = start_coordinates
    x,y = convert_pos_to_int(start_coordinates)

    pygame.draw.rect(show_world_generation.WIN, (255, 255, 255),
    pygame.Rect(show_world_generation.TILESIZE * x, show_world_generation.TILESIZE * y, show_world_generation.TILESIZE, show_world_generation.TILESIZE))
    pygame.display.flip()

    path = []
    exclude = []

    while True:
        skip = False
        for i, e in enumerate(OFFSET):
            if skip:
                break
            if i == 4:
                continue
            curpos = convert_pos_to_int(current_pos)
            offpos = convert_pos_to_int(e)
            temp_pos = f"{curpos[0] + offpos[0]} {curpos[1] + offpos[1]}"
            if world_map.get(temp_pos) == target_value: # Tile is invalid
                continue
            if temp_pos not in path and temp_pos not in exclude:
                for i, element in enumerate(OFFSET):
                    if i % 2 == 1 and not skip:                        
                        x,y = convert_pos_to_int(temp_pos) # FOR DRAWING
                        pygame.draw.rect(show_world_generation.WIN, (255, 0 , 0), 
                        pygame.Rect(show_world_generation.TILESIZE * x, show_world_generation.TILESIZE * y, show_world_generation.TILESIZE, show_world_generation.TILESIZE))
                        pygame.display.flip()

                        pygame.draw.rect(show_world_generation.WIN, (255, 0 , 0), 
                        pygame.Rect(show_world_generation.TILESIZE * x, show_world_generation.TILESIZE * y, show_world_generation.TILESIZE, show_world_generation.TILESIZE))
                        pygame.display.flip()

                        curpos = convert_pos_to_int(temp_pos)
                        offpos = convert_pos_to_int(element)
                        offset_pos = f"{curpos[0] + offpos[0]} {curpos[1] + offpos[1]}"
                        if world_map.get(offset_pos) == target_value: # Valid pos
                            skip = True
                            current_pos = temp_pos
                            path.append(temp_pos)

            for i, e in enumerate(path): # Only for visual representation
                color = (235, 79, 52)
                if i == len(path) - 1:
                    color = (133, 92, 62)
                x,y = convert_pos_to_int(e)
                pygame.draw.rect(show_world_generation.WIN, color, 
                pygame.Rect(show_world_generation.TILESIZE * x, show_world_generation.TILESIZE * y, show_world_generation.TILESIZE, show_world_generation.TILESIZE))
                pygame.display.flip()
            time.sleep(1)

    return world_map

def convert_pos_to_int(pos) -> list:
    lst = []
    for e in pos.split(" "):
        lst.append(int(e))
    return lst