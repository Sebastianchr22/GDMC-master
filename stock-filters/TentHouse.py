from Structure import Structure
import Builder

plank           = (5, 0)
grass           = (2, 0)
fence           = (85, 0)
wool            = (35, 0)
empty           = (0, 0)
cake            = (92, 0)
furnace         = (62, 2)
bed_lower       = (26, 1)
bed_upper       = (26, 9)

class TentHouse(Structure): #inheritance
    blueprint_north = [
        [
            [wool, wool, wool, wool, wool],
            [bed_lower, bed_upper, fence, bed_upper, bed_lower],
            [wool, wool, wool, wool, wool]
        ],
        [
            [wool, wool, wool, wool, wool],
            [empty, empty, fence, empty, empty],
            [wool, wool, wool, wool, wool]
        ],
        [
            [empty, empty, empty, empty, empty],
            [wool, wool, wool, wool, wool],
            [empty, empty, empty, empty, empty]
        ],
        [
            [empty, empty, empty, empty, empty],
            [wool, wool, wool, wool, wool],
            [empty, empty, empty, empty, empty]
        ]
        
    ]
    
    blueprint_east = [
        [
            [wool, bed_lower, wool],
            [wool, bed_upper, wool],
            [wool, fence, wool],
            [wool, bed_upper, wool],
            [wool, bed_lower, wool],
        ],
        [
            [wool, empty, wool],
            [wool, empty, wool],
            [wool, fence, wool],
            [wool, empty, wool],
            [wool, empty, wool],
        ],
        [
            [empty, wool, empty],
            [empty, wool, empty],
            [empty, wool, empty],
            [empty, wool, empty],
            [empty, wool, empty],
        ],
        [
            [empty, wool, empty],
            [empty, wool, empty],
            [empty, wool, empty],
            [empty, wool, empty],
            [empty, wool, empty],
        ]
        
    ]

    


    pattern_east = [
        #Facing east (east = x+)
        (-1,-1), (-1,0), (-1,1),
        (-2,-1), (-2,0), (-2,1),
        (-3,-1), (-3,0), (-3,1),
        (-4,-1), (-4,0), (-4,1),
        (-5,-1), (-5,0), (-5,1)
    ]
    pattern_west = [
        #Facing west (west = x-)
        (1,-1), (1,0), (1,1),
        (2,-1), (2,0), (2,1),
        (3,-1), (3,0), (3,1),
        (4,-1), (4,0), (4,1),
        (5,-1), (5,0), (5,1)
    ]
    pattern_north = [
        #Facing North (north = z-)
        (1,-1), (0,-1), (-1,-1),
        (1,-2), (0,-2), (-1,-2),
        (1,-3), (0,-3), (-1,-3),
        (1,-4), (0,-4), (-1,-4), 
        (1,-5), (0,-5), (-1,-5)
    ]
    pattern_south = [
        #Facing South (south = z+)
        (-1,1), (0,1), (1,1),
        (-1,2), (0,2), (1,2),
        (-1,3), (0,3), (1,3),
        (-1,4), (0,4), (1,4), 
        (-1,5), (0,5), (1,5)
    ]

    origins =       [(-1,-5),            (-5,-1),             (-1,0),              (1,-1)]
    patterns =      [pattern_north,     pattern_east,       pattern_south,      pattern_west]
    blueprints =    [blueprint_north,   blueprint_east,     blueprint_north,    blueprint_east] #Mirrored for west and south
