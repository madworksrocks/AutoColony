class Tile:

    def __init__(self, main):
        self.main = main

tile_ids_start = 0
tile_ids = []
def add_to_tile_ids(func):
    global tile_ids
    tile_ids.append(func)

    return func


# @add_to_tile_ids
class Template(Tile):
    requires_instance_data = False
    def __init__(self, main, data = None):
        super().__init__(main)

        self.load_data(data)

    def load_data(self, data):
        if data is None:
            pass

        else:
            pass

    def compress_data(self):
        data = ""

        return data


@add_to_tile_ids
class Air(Tile):
    requires_instance_data = False
    def __init__(self, main, data = None):
        super().__init__(main)

        self.load_data(data)

    def load_data(self, data):
        if data is None:
            pass

        else:
            pass

    def compress_data(self):
        data = ""

        return data


@add_to_tile_ids
class Soil(Tile):
    requires_instance_data = False
    def __init__(self, main, data = None):
        super().__init__(main)

        self.load_data(data)

    def load_data(self, data):
        if data is None:
            pass

        else:
            pass

    def compress_data(self):
        data = ""

        return data


@add_to_tile_ids
class Stone(Tile):
    requires_instance_data = False
    def __init__(self, main, data = None):
        super().__init__(main)

        self.load_data(data)

    def load_data(self, data):
        if data is None:
            pass

        else:
            pass

    def compress_data(self):
        data = ""

        return data
