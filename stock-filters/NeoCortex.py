from math import sqrt
from PrefrontalCortex import Impulse
from Decisions import Decisions
from Decision import Decision

import random as rand

# The job of the Neo-cortex is to evaluate, think, and consider.
# It is a slow brain part, but a highly important one, it's job is to perform tasks for the prefrontal cortex (to make it happy), 
#       While finding the optimal ways to do those tasks.

class NeoCortex:
    def __init__(self, settler, world_grid):
        self.settler = settler
        self.decision_tree = self.settler._get_decisions()
        self.world_grid = world_grid
        self.xz_grid = self.get_xz_of(world_grid[:])
    
    def get_xz_of(self, grid):
        l = []
        for cell in grid:
            c = []
            for block in cell.get_chunk():
                c.append((block[0], block[2]))
            l.append(c)
        return l

    def handle_impulse(self, impulse, weights):
        text = ""
        if impulse.name == Impulse.WANT_FOOD.name:
            food = self._go_hunt()
            if food > 0:
                text = "Went to hunt, and found "+ str(food) +" food!"
            else:
                text = "Went to hunt, and found nothing.."
        
        elif impulse.name == Impulse.WANT_SHELTER.name:
            text = self._go_build_shelter()
        
        elif impulse.name == Impulse.WANT_SLEEP.name:
            self._go_sleep()
            text = "Went to sleep"
        
        elif impulse.name == Impulse.WANT_CHILDREN.name:
            if self.settler._get_has_mate():
                self._go_mate()
            else:
                self._go_find_mate()
            text = "Went to mate"
        #print "SETTLER: ", text
        decision = Decision(text, impulse, weights)
        self.decision_tree.new_decision(decision)

    #Returns a boolean value true if the settler found food after hunting
    def _go_hunt(self):
        self.settler._move(self.find_free_grid_cell()) #Action
        success_prob = 0.5
        bounds = (0, 10)
        found_food = rand.randrange(bounds[0], bounds[1], 1) >= bounds[1] * success_prob
        food = int(found_food) * int(rand.randrange(0, 2))
        self.settler.add_food(food)
        return food

    def _go_build_shelter(self):
        if self.can_build():
            self.settler.settlement.settler_claims_index(self.settler.origin)
            self.settler._build() #Action
            self.world_grid[self.settler.origin].use_segment() #Mental note
            self.settler.set_has_shelter()
            return "Succesfully built a shelter"
        else: #Either too close to another house, or already occupied
            self.settler._move(self.find_free_grid_cell()) #Action
            return "Went to build shelter, but cell was occupied or too close to other shelter"

    def _go_sleep(self):
        pass
    
    def _go_mate(self):
        self.settler._mate()
    
    def _go_find_mate(self):
        self.settler._move_to_other_settler()

    def can_build(self):
        s = self.world_grid[self.settler.origin].get_chunk()[0]
        dist = 0
        if self.settler.settlement.get_index_claimed(self.settler.origin):
            return False
        for house_index in self.settler.settlement.get_all_shelter_indexes():
            t = self.world_grid[house_index].get_chunk()[0]
            dist = (s[0] - t[0], s[2] - t[2])
            dist = (pow(dist[0], 2), pow(dist[1], 2))
            dist = (int(sqrt(dist[0])), int(sqrt(dist[1])))
            if dist[0] <= 10 and dist[1] <= 10:
                    return False
        return True
    
    def find_free_grid_cell(self):
        point = self.world_grid[self.settler.origin].get_chunk()[0] #Initial and fallback (no move)
        attempts = 0
        new_point = (self.get_step_size(point[0]), self.get_step_size(point[2]))

        while not self.point_in_grid(new_point, self.xz_grid):
            new_point = (self.get_step_size(point[0]), self.get_step_size(point[2]))
            if self.settler.steps_left <= 0:
                print "Settler died thinking"
                return self.settler.origin          
            if attempts % 5 == 0: #Slowly die trying to move (prevents stalling)
                self.settler.steps_left -= 1
            attempts += 1

        return self.get_index_of(new_point, self.xz_grid)
    
    def get_step_size(self, loc):
        d = 5 #One chunk per step
        return int(rand.normalvariate(loc, d))
    
    def point_in_grid(self, point, grid):
        for cell in grid:
            if point in cell:
                return True
        return False

    def get_index_of(self, point, grid):
        for cell in grid:
            if point in cell:
                return grid.index(cell)
        return 0