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
    path = []
    x,y = convert_pos_to_int(start_coordinates)

    pygame.draw.rect(show_world_generation.WIN, (255, 255, 255), 
    pygame.Rect(show_world_generation.TILESIZE * x, show_world_generation.TILESIZE * y, show_world_generation.TILESIZE, show_world_generation.TILESIZE))
    pygame.display.flip()

    while True:
        for e in OFFSET:
            time.sleep(1)
            curpos = convert_pos_to_int(current_pos)
            offpos = convert_pos_to_int(e)
            current_pos = f"{curpos[0] + offpos[0]} {curpos[1] + offpos[1]}" # Is the actual coordinate
            if world_map.get(current_pos) == target_value: # We want a tile that does not have target tile so we skip
                continue
            print(current_pos)

            x,y = convert_pos_to_int(current_pos)[0], convert_pos_to_int(current_pos)[1]

            pygame.draw.rect(show_world_generation.WIN, (204, 0, 255), 
            pygame.Rect(show_world_generation.TILESIZE * x, show_world_generation.TILESIZE * y, show_world_generation.TILESIZE, show_world_generation.TILESIZE))
            pygame.display.flip()

            if current_pos == start_coordinates:
                break
            for i, n in enumerate(OFFSET):
                if i % 2 == 1 and i != 0: # If valid index we only want indexes 1 3 5 7
                    curpos = convert_pos_to_int(current_pos)
                    offpos = convert_pos_to_int(n)
                    offset_pos = f"{curpos[0] + offpos[0]} {curpos[1] + offpos[1]}" #
                    #print(i, world_map.get(offset_pos), target_value, "VALUES AND INDEX")
                    if world_map.get(offset_pos) == target_value:
                        valid_coordinate = True
                        for pos in path:
                            if pos == current_pos:
                                valid_coordinate = False
                                break

                        if valid_coordinate:
                            path.append(current_pos)
                            print(current_pos, "ADDING VALUE")
                            world_map[current_pos] = -11

                            x,y = convert_pos_to_int(current_pos)[0], convert_pos_to_int(current_pos)[1]
                            pygame.draw.rect(show_world_generation.WIN, (204, 0, 255), 
                            pygame.Rect(show_world_generation.TILESIZE * x, show_world_generation.TILESIZE * y, show_world_generation.TILESIZE, show_world_generation.TILESIZE))
                            pygame.display.flip()

    return world_map

def convert_pos_to_int(pos) -> list:
    lst = []
    for e in pos.split(" "):
        lst.append(int(e))
    return lst