from typing import Set

from Settler import Settler
import random as rand


class Settlement:
    def __init__(self, n, s, level, world_grid):
        self.settlers = []
        self.level = level
        self.world_grid = world_grid
        self.settler_steps = s
        for settler in range(0, n):
            self.create_new_settler()

    def step(self):
        print("Simulating ", len(self.settlers), " settlers for this step")
        for settler in self.settlers:
            if settler.steps_left > 0:
                settler.step()
    
    def create_new_settler(self):
        self.settlers.append(
            Settler(self.level, self.world_grid, int(len(self.world_grid) / 2), self, self.settler_steps)
        )

    def get_settlement_level(self):
        return self.level

    def get_random_settler(self):
        return self.settlers[int(rand.randrange(0, len(self.settlers)))]

    def new_child(self, of_settler1, of_settler2):
        self.settlers.append(
            Settler(self.level, self.world_grid, of_settler1.origin, self, 25)
        )

    def get_all_settlers(self):
        return self.settlers
