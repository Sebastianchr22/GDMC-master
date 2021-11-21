from enum import Enum
import random as r

class Impulse(Enum):
    WANT_FOOD = 0
    WANT_SLEEP = 1
    WANT_SHELTER = 2
    WANT_CHILDREN = 3

# The job of the Prefrontal cortex is to control behaviour in coordination with internal goals.
# This brain is impulse driven, and rather fast.
class PrefrontalCortex:
    def __init__(self, settler):
        self.settler = settler #The body of the brain
    
    def get_impulse(self):
        weights = self.weigh_impulses()
        heighest_weighted_impulse = self.get_highest_weighed_impulse(weights)
        return Impulse(heighest_weighted_impulse), weights

    def weigh_impulses(self):
        impulses = {0: self.settler._get_hunger(), 1:0, 2:0, 3:0}
        impulses[2] = 0.03

        #Impulse to mate
        if self.settler._get_hunger() <= 0.5 and self.settler._get_has_shelter():
            #Having children becomes a priority when basic needs are met
            impulses[3] = 2 / (self.settler._get_children_num() + 1) #Avoid division by zero
        
        #Impulse to build a house:
        if self.settler._get_hunger() <= 0.7 and not self.settler._get_has_shelter():
            impulses[2] = 1 - self.settler._get_hunger()
        
        #Impulse to eat
        if self.settler._get_hunger() >= 0.7:
            impulses[0] = 1

        return impulses

    def get_highest_weighed_impulse(self, weights):
        highest_index = 0
        for index in weights:
            if weights[index] > weights[highest_index]:
                highest_index = index
        return highest_index