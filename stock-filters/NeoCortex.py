from PrefrontalCortex import Impulse
from Decisions import Decisions
from Decision import Decision

# The job of the Neo-cortex is to evaluate, think, and consider.
# It is a slow brain part, but a highly important one, it's job is to perform tasks for the prefrontal cortex (to make it happy), 
#       While finding the optimal ways to do those tasks.

class NeoCortex:
    def __init__(self, settler, world_grid, origin) -> None:
        self.settler = settler
        self.decision_tree = self.settler._get_decisions()
        self.world_grid = world_grid
        self.origin = origin
        print("Creating Neo-Cortex")
    
    def handle_impulse(self, impulse : Impulse, weights : dict) -> None:
        print(impulse)
        text = ""
        if impulse == Impulse.WANT_FOOD:
            self._go_hunt()
            text = "Went hunting for food"
        
        elif impulse == Impulse.WANT_SHELTER:
            self._go_build_shelter()
            text = "Went to build a shelter"
        
        elif impulse == Impulse.WANT_SLEEP:
            self._go_sleep()
            text = "Went to sleep"
        
        elif impulse == Impulse.WANT_CHILDREN:
            self._go_mate()
            text = "Went to mate"

        decision = Decision(text, impulse, weights)
        self.decision_tree.new_decision(decision)

    def _go_hunt(self) -> None:
        print("Going hunting")

    def _go_build_shelter(self) -> None:
        print("Building shelter")

    def _go_sleep(self) -> None:
        print("Sleeping... zzZZzz...")
    
    def _go_mate(self) -> None:
        print("Mating..")
