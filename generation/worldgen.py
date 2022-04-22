import random

import generation.refineworld
import generation.value

def generate_world(width, height, **kwargs):

    '''
    volatility is how much a tile varies from its neighboring tiles. 
    Higher volatility brings more randomness.
    Lower is less randomness.


    Since the generation "smoothes" the world by using averages.
    The trend is an island to the top left corner of the game screen, and the rest water.
    Thats were the survivability offset comes in.
    This variable helps stabilize the world.
    survivability_offset = 2 <- by default.
    '''
    
    volatility = 1
    survivability_offset = 2

    for k in kwargs:
        if k == "volatility":
            volatility = kwargs.get(k)
        elif k == "survivability_offset":
            survivability_offset = kwargs.get(k)

    world = primitive_generate(width, height, volatility, survivability_offset)
    world = generation.refineworld.smooth_world(world, width, height)

    return world

def primitive_generate(width, height, volatility, survivability_offset):
    world_map = {}
    value = random.randrange(0, 100)
    for y in range(height):
        for x in range(width):
            pos = f"{x} {y}"
            if y == 0:
                world_map[pos] = random.randrange(0, 100)
                continue
            value = modify_value(world_map, value, pos, volatility, survivability_offset)
            world_map[pos] = value
    return world_map

def modify_value(worldmap, value, pos, volatility, survivability_offset):
    
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
        new_value = int(average + random.randrange(-volatility, volatility + survivability_offset))

    new_value = generation.value.check_value(new_value)
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