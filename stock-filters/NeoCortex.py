from PrefrontalCortex import Impulse
from Decisions import Decisions
from Decision import Decision

import Builder as build
import random as rand

# The job of the Neo-cortex is to evaluate, think, and consider.
# It is a slow brain part, but a highly important one, it's job is to perform tasks for the prefrontal cortex (to make it happy), 
#       While finding the optimal ways to do those tasks.

class NeoCortex:
    def __init__(self, settler, level, world_grid, origin) -> None:
        self.settler = settler
        self.level = level
        self.decision_tree = self.settler._get_decisions()
        self.world_grid = world_grid
        self.origin = origin
        print("Creating Neo-Cortex")
    
    def handle_impulse(self, impulse : Impulse, weights : dict) -> None:
        text = ""
        if impulse == Impulse.WANT_FOOD:
            food = self._go_hunt()
            if food > 0:
                text = "Went to hunt, and found "+ str(food) +" food!"
                self.settler.add_food(food)
            else:
                text = "Went to hunt, and found nothing.."
        
        elif impulse == Impulse.WANT_SHELTER:
            self._go_build_shelter()
            text = "Went to build a shelter"
        
        elif impulse == Impulse.WANT_SLEEP:
            self._go_sleep()
            text = "Went to sleep"
        
        elif impulse == Impulse.WANT_CHILDREN:
            if self.settler._get_has_mate():
                self._go_mate()
            else:
                self._go_find_mate()
            text = "Went to mate"

        decision = Decision(text, impulse, weights)
        self.decision_tree.new_decision(decision)

    #Returns a boolean value true if the settler found food after hunting
    def _go_hunt(self) -> int:
        loc = rand.normalvariate(self.origin, 1)
        self.origin = (self.origin + int(abs(loc))) % len(self.world_grid)
        success_prob = 0.5
        bounds = (0, 10)
        found_food = rand.randrange(bounds[0], bounds[1], 1) >= bounds[1] * success_prob
        food = int(found_food) * int(rand.randrange(0, 2))
        return food

    def _go_build_shelter(self) -> None:
        origin_point = self.world_grid[self.origin]
        build.build_temp_house(self.level, origin_point)

    def _go_sleep(self) -> None:
        print("Sleeping... zzZZzz...")
        pass
    
    def _go_mate(self) -> None:
        print("Mating..")

    
    def _go_find_mate(self) -> None:
