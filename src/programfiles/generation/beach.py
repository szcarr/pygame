import random


import generation.circumference.circumference as circumference
import tiles.tiles as tiles
import generation.worldgen as worldgen

def generate_beach(water_start_coordinates, world_map, tilelist):

    sand_value = tiles.get_tile_by_name(tilelist, "Sand").tile_id
    deep_water_value = tiles.get_tile_by_name(tilelist, "Deep water").tile_id

    ocean_outline = circumference.draw_outline(deep_water_value, water_start_coordinates, world_map)

    # need to determine the direction of the sand
    for selected_value in ocean_outline:
        obj_dir = [False, False, False, False] # 0 = North, 1 = East, 2 = South, 3 = West
        selx, sely = worldgen.convert_pos_to_int(selected_value)
        for e in ocean_outline: # Determine direction
            selx, sely = worldgen.convert_pos_to_int(selected_value)
            ex, ey = worldgen.convert_pos_to_int(e)
            if ey > sely and selx == ex:
                obj_dir[0] = True
            elif ey < sely and selx == ex:
                obj_dir[2] = True
            if ex > selx and sely == ey:
                obj_dir[1] = True
            if ex < selx and sely == ey:
                obj_dir[3] = True
        for i, e in enumerate(obj_dir):
            amount_of_sand_tiles_to_generate = random.randrange(2, 4)
            if i == 0 and e:
                for y in range(amount_of_sand_tiles_to_generate):
                    current_pos = f"{selx} {sely - y}"
                    world_map[current_pos] = sand_value
            elif i == 1 and e:
                for x in range(amount_of_sand_tiles_to_generate):
                    current_pos = f"{selx + x} {sely}"
                    world_map[current_pos] = sand_value
            elif i == 2 and e:
                for y in range(amount_of_sand_tiles_to_generate):
                    current_pos = f"{selx} {sely + y}"
                    world_map[current_pos] = sand_value
            elif i == 3 and e:
                for x in range(amount_of_sand_tiles_to_generate):
                    current_pos = f"{selx - x} {sely}"
                    world_map[current_pos] = sand_value

    return world_map