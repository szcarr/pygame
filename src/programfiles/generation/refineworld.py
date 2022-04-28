import random

import generation.value

def smooth_world(world_map, width, height, offset_value, hard_smoothing):
    # offset_value for more variation
    average_value = 0
    for y in range(height):
        for x in range(width):
            pos = f"{x} {y}"
            lst = get_neighbors_from(world_map, pos)
            if hard_smoothing:
                average_value = hard_average(lst)
            else:
                average_value = soft_average(lst)
            if offset_value != 0:
                world_map[pos] = generation.value.check_value(average_value + random.randrange(-offset_value, offset_value))
            else:
                world_map[pos] = average_value
    return world_map

def get_neighbors_from(world_map, coords):
    
    offset = [
        "-1 -1", "0 -1", "1 -1",
        "-1 0", "1 0",
        "-1 1", "0 1", "1 1",
    ]

    neighbors = []
    for i, e in enumerate(offset):
        currentX, currentY = convert_pos_to_int(coords)[0] + convert_pos_to_int(e)[0], convert_pos_to_int(coords)[1] + convert_pos_to_int(e)[1]
        k = str(currentX) + " " + str(currentY)
        tile_value = world_map.get(k)
        if tile_value != None:
            neighbors.append(tile_value)

    return neighbors

def convert_pos_to_int(pos):
    lst = []
    for e in pos.split(" "):
        lst.append(int(e))
    return lst

def soft_average(lst):
    sum_values = 0
    for e in lst:
        sum_values = sum_values + int(e)
    average = sum_values / len(lst)
    return int(round(average))

def hard_average(lst):
    val = {}
    for e in lst:
        if e not in val:
            val[e] = 1
        else:
            val[e] = val.get(e) + 1

    equals = []
    highest_number = -1
    for k in val:
        if val.get(k) > highest_number:
            highest_number = val.get(k)
            equals.clear()
            equals.append(k)
        elif val.get(k) == highest_number:
            equals.append(k)                

    ri = random.randrange(0, len(equals))
    value = equals[ri]
    return value