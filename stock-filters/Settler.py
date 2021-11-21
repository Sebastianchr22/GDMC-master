#Settlers are the agents of simulation in this project. 
# An agent will be bord with a brain of two components: 
#       - The prefrontal cortex (impulsive, and controlling in order to achieve personal goals) also called 'system 1'
#       - The neo-cortex (thoughtful, decision making part) also called 'system 2'

from NeoCortex import NeoCortex
from PrefrontalCortex import PrefrontalCortex
from Decisions import Decisions
import random as rand
import Builder as build


####To implement: All world grids must contains all its blocks, and all settlers upon the cell.

class Settler:
    def __init__(self, level, world_grid, origin, settlement, steps):
        self.decisions = Decisions()
        self.system1 = PrefrontalCortex(self)
        self.system2 = NeoCortex(self, world_grid)
        self.level = level
        self.world_grid = world_grid
        self.origin = origin
        self.has_shelter = False
        self.food = 1
        self.has_mate = False
        self.children = 0
        self.settlement = settlement
        self.steps_left = steps

    def step(self):
        impulse, weights = self.system1.get_impulse()
        self.system2.handle_impulse(impulse, weights)

    #Hunger is proportionally small compared to the supply of food available to the settler
    def _get_hunger(self):
        return 1/self.food
    
    def add_food(self, food):
        self.food += food

    def _get_has_shelter(self):
        return self.has_shelter
    
    def set_has_shelter(self):
        self.has_shelter = True

    def _get_has_mate(self):
        return self.has_mate
    
    def set_has_mate(self):
        self.has_mate = True

    def _get_children_num(self):
        return self.children

    def add_children(self, num):
        self.children += num

    def _get_decisions(self):
        return self.decisions

    def _move(self):
        self.world_grid[self.origin].remove_settler(self)
        point = self.world_grid[self.origin].get_chunk()[0]
        loc = (self._get_step_dist(point[0]), self._get_step_dist(point[2]))
        for seg in self.world_grid:
            c = seg.get_chunk()
            for block in c:
                if block[0] == loc[0] and block[2] == loc[1]:
                    self.origin = self.world_grid.index(seg)
                    seg.add_settler(self)
                    break

        #self.origin = (self.origin + int(loc)) % len(self.world_grid)
        #self.world_grid[self.origin].add_settler(self)

    def _get_step_dist(self, origin):
        return int(rand.normalvariate(origin, 15))

    def _build(self):
        build.build_temp_house(self.level, self.world_grid[self.origin])

    def _mate(self, mate):
        self.settlement.new_child(self, mate)

    def _move_to_other_settler(self):
        mate = self.settlement.get_random_settler()
        #Random chance of concent
        if rand.randrange(0,2) > 0.5:
            mate.origin = self.origin #Mate moves in :D
            children_num = rand.randrange(0,2)
            for child in range(0, children_num):
                self._mate(mate)
            self.steps_left = 0
            mate.steps_left = 0
            print("Mating complete, created ", children_num, " children")


