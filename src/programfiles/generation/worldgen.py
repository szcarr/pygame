import random
import math

import generation.refineworld
import generation.value
import tiles.tiles as tiles
import generation.circumference.circumference as circumference

def generate_world(width, height, tilelist ,**kwargs):

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

    world = generate_plains(width, height, tilelist)
    world = generation.refineworld.smooth_world(world, width, height)

    return world

def generate_plains(width, height, tilelist):

    world_map = {}

    value = tiles.get_tile_by_name(tilelist, "Grass").tile_id

    for y in range(height):
        for x in range(width):
            pos = f"{x} {y}"
            world_map[pos] = value
    return world_map

def generate_ocean(ocean_size, number_of_oceans, world_map, generating_position, tilelist):

    value = tiles.get_tile_by_name(tilelist, "Deep water").tile_id

    total_ocean_map = {}

    offset = [
        "0 -1", "-1 0", "1 0", "0 1",
    ]

    for o in range(number_of_oceans):
        ocean_map = {}

        if o == 0:
            ocean_map[generating_position] = value
        else:
            roll_random_index = random.randint(0, len(total_ocean_map)) # <- Random index to start new ocean from
            counter = 0
            start_index = "0 0"
            for k in total_ocean_map:
                if counter == roll_random_index:
                    start_index = k
                counter += 1

            right = True if random.randint(0, 1) == 1 else False
            up = True if random.randint(0, 1) == 1 else False
            counter = 0

            index = start_index
            while True:
                if right:
                    index = f"{convert_pos_to_int(index)[0] + 1} {convert_pos_to_int(index)[1]}"
                else:
                    index = f"{convert_pos_to_int(index)[0] - 1} {convert_pos_to_int(index)[1]}"
                if up:
                    index = f"{convert_pos_to_int(index)[0]} {convert_pos_to_int(index)[1] - 1}"
                else:
                    index = f"{convert_pos_to_int(index)[0]} {convert_pos_to_int(index)[1] + 1}"
                if total_ocean_map.get(index) != value:
                    start_index = index
                    break
            ocean_map[start_index] = value

        current_ocean_size = 0
        while current_ocean_size != ocean_size and current_ocean_size <= ocean_size:
            roll_random_index = random.randint(0, len(ocean_map)) 
            i = 0
            ocean_map_copy = ocean_map.copy()
            for key in ocean_map_copy:
                if i == roll_random_index:
                    for e in offset:
                        offset_pos = f"{convert_pos_to_int(key)[0] + convert_pos_to_int(e)[0]} {convert_pos_to_int(key)[1] + convert_pos_to_int(e)[1]}"
                        if ocean_map_copy.get(offset_pos) != value:
                            ocean_map[offset_pos] = value
                            current_ocean_size += 1
                i += 1
        for k in ocean_map:
            total_ocean_map[k] = ocean_map.get(k)

    for k in total_ocean_map:
        world_map[k] = total_ocean_map.get(k)

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