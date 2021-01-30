import numpy as np
import json

class Main:
    world_shape = (100,100,100)
    # tile_size = 11  # length of tile key(1 char), tile key, instance key
    mmap_mode = None
    
    def __init__(self, main):
        self.main = main
        self.stone_range = (0, 60)
        self.soil_range = (60, 79)
        self.world_middle_surface = (50, 50, 80)

    def create(self, wnf, wkf):
        # self.main.worldnp = np.chararray(self.world_shape, itemsize=self.tile_size)
        self.main.worldnp = np.empty(self.world_shape, dtype=np.int16)
        self.main.worldkeys = []

        self.generate_world(self.main.worldnp)

        np.save(wnf, self.main.worldnp, allow_pickle=False)
        json.dump(self.main.worldkeys, wkf)

    def load(self, wnf, wkf):
        self.main.worldnp = np.load(wnf, mmap_mode=self.mmap_mode, allow_pickle=False)
        self.main.worldkeys = json.load(wkf)

    def save(self, wnf, wkf):
        np.save(wnf, self.main.worldnp, allow_pickle=False)
        json.dump(self.main.worldkeys, wkf)

    def generate_world(self, world):
        world[0:100, 0:100, self.stone_range[0]:self.stone_range[1]] = 2  # Stone
        world[0:100, 0:100, self.soil_range[0]:self.soil_range[1]] = 1  # Soil
