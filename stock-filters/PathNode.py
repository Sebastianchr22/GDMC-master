#The node class used for A* pathfinding in road construction
class Path_node:
    def __init__(self, parent, location, g, h):
        self.location = location
        self.parent = parent
        self.g = g
        self.h = h

    def get_f(self):
        return int(self.g + self.h)

    def get_location(self):
        return self.location
        
    def is_equal_to(self, other):
        return self.location == other.location