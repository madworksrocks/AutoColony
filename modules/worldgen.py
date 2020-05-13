import numpy as np
import json

class Main:
    world_shape = (100,100,100)
    tile_size = 11
    mmap_mode = None
    def __init__(self, main):
        self.main = main

    def create(self, wnf, wkf):
        self.main.worldnp = np.chararray(self.world_shape, itemsize=self.tile_size)
        self.main.worldkeys = {}

        np.save(wnf, self.main.worldnp, allow_pickle=False)
        json.dump(self.main.worldkeys, wkf)

    def load(self, wnf, wkf):
        self.main.worldnp = np.load(wnf, mmap_mode=self.mmap_mode, allow_pickle=False)
        self.main.worldkeys = json.load(wkf)

    def save(self, wnf, wkf):
        np.save(wnf, self.main.worldnp, allow_pickle=False)
        json.dump(self.main.worldkeys, wkf)
