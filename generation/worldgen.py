import random

from numpy import average

def generate(width, height, volatility):
    world_map = {}
    value = random.randrange(0, 100)
    for y in range(height):
        for x in range(width):
            pos = f"{x} {y}"
            value = modify_value(world_map, value, pos, volatility)
            world_map[pos] = value
        
    return world_map

def modify_value(worldmap, value, pos, volatility):
    
    offset = [
        "-1 -1", "0 -1", "1 -1",
        "-1 0",
    ]

    sum_off_values = 0
    number_off_valid_coordinates = 0 # <--- Adds one to this if atttempted value is != None
    for e in offset:
        current_position = convert_pos_to_int(pos)
        offset_index = f"{current_position[0] + convert_pos_to_int(e)[0]} {current_position[1] + convert_pos_to_int(e)[1]}"
        worldmap_value = worldmap.get(offset_index)
        if worldmap_value != None:
            sum_off_values =+ worldmap.get(offset_index)
            number_off_valid_coordinates =+ 1

    is_error = False
    average = 0
    try:
        average = sum_off_values / number_off_valid_coordinates
    except:
        is_error = True

    if is_error:
        new_value = value
    else:
        new_value = int(average + random.randrange(-volatility, volatility))
    return new_value
    
def convert_pos_to_int(pos):
    lst = []
    for e in pos.split(" "):
        lst.append(int(e))
    return lst

def printgeneration(world_map, width, height):
    for y in range(height):
        for x in range(width):
            print(world_map.get(f"{x} {y}"), end=" ")
        print("")

#height = 40
#width = 30


#world = generate(width, height, 3)
#printgeneration(world, width, height)