from Structure import Structure
import Builder

cobble_stone    = (4, 0)
plank           = (5, 0)
log             = (17, 0)
log_side        = (17, 4)
glass           = (20, 0)
door            = 64
door_lower      = (door, 2)
door_upper      = (door, 8)
bed_lower       = (26, 1)
bed_upper       = (26, 9)
empty           = (0, 0)

class CubeHouse(Structure): #inheritance
    blueprint_north = [
        [
            #Floor level
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone]
        ],
        [
            #First level
            [log, plank, plank, plank, log],
            [plank, empty, empty, bed_upper, plank],
            [plank, empty, empty, bed_lower, door_lower],
            [plank, empty, empty, empty, plank],
            [log, plank, plank, plank, log]
        ],
        [
            #Second layer
            [log, plank, glass, plank, log],
            [plank, empty, empty, empty, plank],
            [glass, empty, empty, empty, door_upper],
            [plank, empty, empty, empty, plank],
            [log, plank, glass, plank, log]
        ],
        [
            #Third layer
            [log, plank, plank, plank, log],
            [plank, empty, empty, empty, plank],
            [plank, empty, empty, empty, plank],
            [plank, empty, empty, empty, plank],
            [log, plank, plank, plank, log]
        ],
        [
            #Roof level
            [log, (log[0], 8), (log[0], 8), (log[0], 8), log],
            [log_side, plank, plank, plank, log_side],
            [log_side, plank, plank, plank, log_side],
            [log_side, plank, plank, plank, log_side],
            [log, (log[0], 8), (log[0], 8), (log[0], 8), log]
        ]
    ]
    blueprint_east = [
        [
            #Floor level
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone]
        ],
        [
            #First level
            [log, plank, door_lower, plank, log],
            [plank, empty, empty, bed_upper, plank],
            [plank, empty, empty, bed_lower, plank],
            [plank, empty, empty, empty, plank],
            [log, plank, plank, plank, log]
        ],
        [
            #Second layer
            [log, plank, door_upper, plank, log],
            [plank, empty, empty, empty, plank],
            [glass, empty, empty, empty, glass],
            [plank, empty, empty, empty, plank],
            [log, plank, glass, plank, log]
        ],
        [
            #Third layer
            [log, plank, plank, plank, log],
            [plank, empty, empty, empty, plank],
            [plank, empty, empty, empty, plank],
            [plank, empty, empty, empty, plank],
            [log, plank, plank, plank, log]
        ],
        [
            #Roof level
            [log, (log[0], 8), (log[0], 8), (log[0], 8), log],
            [log_side, plank, plank, plank, log_side],
            [log_side, plank, plank, plank, log_side],
            [log_side, plank, plank, plank, log_side],
            [log, (log[0], 8), (log[0], 8), (log[0], 8), log]
        ]
    ]
    blueprint_south = [
        [
            #Floor level
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone]
        ],
        [
            #First level
            [log, plank, plank, plank, log],
            [plank, empty, empty, bed_upper, plank],
            [door_lower, empty, empty, bed_lower, plank],
            [plank, empty, empty, empty, plank],
            [log, plank, plank, plank, log]
        ],
        [
            #Second layer
            [log, plank, glass, plank, log],
            [plank, empty, empty, empty, plank],
            [door_upper, empty, empty, empty, glass],
            [plank, empty, empty, empty, plank],
            [log, plank, glass, plank, log]
        ],
        [
            #Third layer
            [log, plank, plank, plank, log],
            [plank, empty, empty, empty, plank],
            [plank, empty, empty, empty, plank],
            [plank, empty, empty, empty, plank],
            [log, plank, plank, plank, log]
        ],
        [
            #Roof level
            [log, (log[0], 8), (log[0], 8), (log[0], 8), log],
            [log_side, plank, plank, plank, log_side],
            [log_side, plank, plank, plank, log_side],
            [log_side, plank, plank, plank, log_side],
            [log, (log[0], 8), (log[0], 8), (log[0], 8), log]
        ]
    ]
    blueprint_west = [ #Currently facing east
        [
            #Floor level
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone],
            [cobble_stone, cobble_stone, cobble_stone, cobble_stone, cobble_stone]
        ],
        [
            #First level
            [log, plank, plank, plank, log],
            [plank, empty, empty, bed_upper, plank],
            [plank, empty, empty, bed_lower, plank],
            [plank, empty, empty, empty, plank],
            [log, plank, door_lower, plank, log]
        ],
        [
            #Second layer
            [log, plank, glass, plank, log],
            [plank, empty, empty, empty, plank],
            [glass, empty, empty, empty, glass],
            [plank, empty, empty, empty, plank],
            [log, plank, door_upper, plank, log]
        ],
        [
            #Third layer
            [log, plank, plank, plank, log],
            [plank, empty, empty, empty, plank],
            [plank, empty, empty, empty, plank],
            [plank, empty, empty, empty, plank],
            [log, plank, plank, plank, log]
        ],
        [
            #Roof level
            [log, (log[0], 8), (log[0], 8), (log[0], 8), log],
            [log_side, plank, plank, plank, log_side],
            [log_side, plank, plank, plank, log_side],
            [log_side, plank, plank, plank, log_side],
            [log, (log[0], 8), (log[0], 8), (log[0], 8), log]
        ]
    ]


    #Patters represent the block ids, 
    pattern_east = [
        #Facing east (east = x+) thus starting from 1 to distance from the road
        (1,-2), (1,-1), (1,0), (1, 1), (1, 2), 
        (2,-2), (2,-1), (2,0), (2, 1), (2, 2), 
        (3,-2), (3,-1), (3,0), (3, 1), (3, 2), 
        (4,-2), (4,-1), (4,0), (4, 1), (4, 2), 
        (5,-2), (5,-1), (5,0), (5, 1), (5, 2)
    ]
    pattern_west = [
        #Facing west (west = x-)
        (-5,-2), (-5,-1), (-5,0), (-5, 1), (-5, 2),
        (-4,-2), (-4,-1), (-4,0), (-4, 1), (-4, 2), 
        (-3,-2), (-3,-1), (-3,0), (-3, 1), (-3, 2), 
        (-2,-2), (-2,-1), (-2,0), (-2, 1), (-2, 2), 
        (-1,-2), (-1,-1), (-1,0), (-1, 1), (-1, 2)
    ]
    pattern_north = [
        #Facing North (north = z-)
        (-2,-5), (-1,-5), (0,-5), (1,-5), (2,-5),
        (-2,-4), (-1,-4), (0,-4), (1,-4), (2,-4), 
        (-2,-3), (-1,-3), (0,-3), (1,-3), (2,-3), 
        (-2,-2), (-1,-2), (0,-2), (1,-2), (2,-2), 
        (-2,-1), (-1,-1), (0,-1), (1,-1), (2,-1)
    ]
    pattern_south = [
        #Facing South (south = z+)
        (-2,1), (-1,1), (0,1), (1,1), (2,1), 
        (-2,2), (-1,2), (0,2), (1,2), (2,2), 
        (-2,3), (-1,3), (0,3), (1,3), (2,3), 
        (-2,4), (-1,4), (0,4), (1,4), (2,4), 
        (-2,5), (-1,5), (0,5), (1,5), (2,5)
    ]
    origins =       [(-2,-5),            (1,-2),              (-2,1),              (-5,-2)]
    patterns =      [pattern_north,     pattern_east,       pattern_south,      pattern_west]
    blueprints =    [blueprint_north,   blueprint_east,     blueprint_south,    blueprint_west]