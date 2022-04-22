class Tiles:
    def __init__(self, coordinates, tiletype):
        self.coordinates = coordinates
        self.tile = tiletype

class TileType:
    def __init__(self, name, color, value):
        self.name = name
        self.color = color
        self.value = value