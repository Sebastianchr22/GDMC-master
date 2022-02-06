#The superclass of all housing classes,
#This is responsible for checking if the structure fits onto a spot, and to handle the blueprint 
class Structure:
    #blueprint = [[[]]] #3d Representation of the house where each cell is a block id (row 1 = x, row 2 = z and row 3 = y)
    #pattern = [[]] #A  2d representation of the freespace needed to build the house (not accounting for the presence of a road nearby)

    def get_blueprints(self):
        return self.blueprints
    
    def get_patterns(self):
        return self.patterns
    
    def get_origins(self):
        return self.origins