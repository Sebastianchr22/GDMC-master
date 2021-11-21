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
    
    def handle_impulse(self, impulse, weights):
        text = ""
        if impulse.name == Impulse.WANT_FOOD.name:
            food = self._go_hunt()
            if food > 0:
                text = "Went to hunt, and found "+ str(food) +" food!"
            else:
                text = "Went to hunt, and found nothing.."
        
        elif impulse.name == Impulse.WANT_SHELTER.name:
            self._go_build_shelter()
            text = "Went to build a shelter"
        
        elif impulse.name == Impulse.WANT_SLEEP.name:
            self._go_sleep()
            text = "Went to sleep"
        
        elif impulse.name == Impulse.WANT_CHILDREN.name:
            if self.settler._get_has_mate():
                self._go_mate()
            else:
                self._go_find_mate()
            text = "Went to mate"

        decision = Decision(text, impulse, weights)
        self.decision_tree.new_decision(decision)

    #Returns a boolean value true if the settler found food after hunting
    def _go_hunt(self):
        self.settler._move() #Action
        success_prob = 0.5
        bounds = (0, 10)
        found_food = rand.randrange(bounds[0], bounds[1], 1) >= bounds[1] * success_prob
        food = int(found_food) * int(rand.randrange(0, 2))
        self.settler.add_food(food)
        return food

    def _go_build_shelter(self):
        if self.can_build():
            self.settler._build() #Action
            self.world_grid[self.settler.origin].use_segment() #Mental note
            self.settler.set_has_shelter()
        else: #Either too close to another house, or already occupied
            self.settler._move() #Action

    def _go_sleep(self):
        pass
    
    def _go_mate(self):
        self.settler._mate()
    
    def _go_find_mate(self):
        self.settler._move_to_other_settler()

    def can_build(self):
        s = self.world_grid[self.settler.origin].get_chunk()[0]
        if self.world_grid[self.settler.origin].get_segment_used():
            return False
        for settler in self.settler.settlement.get_all_settlers():
            if settler._get_has_shelter():
                t = self.world_grid[settler.origin].get_chunk()[0]
                dist = (s[0] - t[0], s[2] - t[2])
                dist = (pow(dist[0], 2), pow(dist[1], 2))
                dist = (int(sqrt(dist[0])), int(sqrt(dist[1])))
                if dist[0] <= 8 or dist[1] <= 8:
                        return False
        return True
    