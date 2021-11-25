from typing import Set

from Settler import Settler
import RoadHandler as RH
import random as rand


class Settlement:
    def __init__(self, n, s, level, world_grid, floor_blocks):
        self.settlers = []
        self.level = level
        self.world_grid = world_grid
        self.floor_blocks = floor_blocks
        self.settler_shelter_indexes = []
        self.settler_steps = s
        for settler in range(0, n):
            self.create_new_settler()

    def step(self):
        #step_text = "Simulation step with ", len(self.settlers), " settlers alive"
        #self.settlement_print(step_text)
        for settler in self.settlers:
            if settler.steps_left > 0:
                settler.step()
            else:
                self.remove_settler(settler)
    
    def create_new_settler(self):
        grid_len = int(len(self.world_grid) / 2)
        loc = int(rand.normalvariate(grid_len, 7))
        self.settlers.append(
            Settler(self.level, self.world_grid, loc, self, self.settler_steps   )
        )

    def get_settlement_level(self):
        return self.level

    def get_random_settler(self):
        return self.settlers[int(rand.randrange(0, len(self.settlers)))]

    def new_child(self, of_settler1, of_settler2):
        self.settlers.append(
            Settler(self.level, self.world_grid, of_settler1.origin, self, int(of_settler1.initial_steps * 0.9))
        )
        #self.settlement_print("A new settlers has been born")

    def get_all_settlers(self):
        return self.settlers

    def get_size_of_settlement(self):
        return len(self.settlers)

    def remove_settler(self, settler):
        self.settlers.remove(settler)
        #self.settlement_print("Settler has lived out their life.")
        self.print_settler_decisions(settler)

    def print_settler_decisions(self, settler):
        print settler._get_decisions().get_decisions_text()

    def settlement_print(self, text):
        print "SETTLEMENT: ", text
        #pass

    def settler_claims_index(self, index):
        self.settler_shelter_indexes.append(index)
        if len(self.settler_shelter_indexes) > 1:
            self.pave_connecting_road()
    
    def get_index_claimed(self, index):
        return index in self.settler_shelter_indexes
    
    def get_all_shelter_indexes(self):
        return self.settler_shelter_indexes
    
    def pave_connecting_road(self):
        shelters = len(self.settler_shelter_indexes) - 1
        fs = self.settler_shelter_indexes[shelters - 1]
        ts = self.settler_shelter_indexes[shelters]
        from_shelter = self.world_grid[fs].get_chunk()[0]
        to_shelter = self.world_grid[ts].get_chunk()[0]
        road = RH.build_road_astar(self.level, from_shelter, to_shelter, self.floor_blocks)
        RH.pave_road(self.level, road)