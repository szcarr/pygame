# Tile colors
BEACH = (214, 191, 88)
DEEP_WATER = (28, 110, 232)
GRASS = (46, 130, 48)
HILLS = (97, 54, 54)
SHALLOW_WATER = (66, 221, 245)
SNOW = (238, 237, 242)
MOUNTAINSBASE = (105, 97, 120)
MOUNTAINSHEAD = (76, 80, 87)

class Tiles: # <- might be useless
    def __init__(self, coordinates, tiletype):
        self.coordinates = coordinates
        self.tile = tiletype

class TileType:
    def __init__(self, name, color, tile_id):
        self.name = name
        self.color = color
        self.tile_id = tile_id        

    def __repr__(self) -> str:
        return f"TileType {self.name} {self.color} {self.tile_id}"

def load_TileTypes():

    tile_list = []

    tiles = {
        "Grass": (46, 130, 48),
        "Shallow water": (214, 191, 88), #(66, 221, 245)
        "Deep water": (28, 110, 232),
        "Sand": (214, 191, 88),
        "Snow": (238, 237, 242),
        "Hills": (97, 54, 54),
        "Moutainbase": (105, 97, 120),
        "Mountainhead": (76, 80, 87),
    }

    tile_id = 0
    for key in tiles:
        value = tiles.get(key)
        tile_list.append(TileType(key, value, tile_id))
        tile_id += 1
    return tile_list

def print_loaded_tiles():
    for e in load_TileTypes():
        print(e.name, e.color, e.tile_id)

def get_tile_by_name(tilelist, name) -> object:
    for e in tilelist:
        if e.name == name:
            return e
    return None # Failed to retrieve

def get_tile_by_id(tilelist, id) -> object:
    for e in tilelist:
        if e.tile_id == id:
            return e
    return None # Failed to retrieve