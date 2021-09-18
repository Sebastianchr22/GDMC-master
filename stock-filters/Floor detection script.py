from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
import random as rand

floor_blocks = []
walkable_blocks = [1,2,3,4,5,12,13]
wool_floor= 171
wool_floor_level = 0

def perform(level, box, options):
    floor_blocks = get_floor_blocks(level, box)
    #uf.setBlock(level, (1,0), x, y, z)
    #print "Floor blocks found: " , len(floor_blocks)

    #mark_floor_blocks(level, floor_blocks)

    road_origin = find_road_origin(floor_blocks)
    mark_road_origin(level, road_origin)

    road_end = find_road_end(floor_blocks)
    mark_road_end(level, road_end)

    path = build_road_astar(level, road_origin, road_end, floor_blocks)
    print "Finished pathfinding"
    for block in path:
        set_block_with_level(level, block[0], block[1], block[2], 4, 0)

    #build_tent(level, floor_blocks[0])

#Will return an array of tuples representing all blocks that are walkable from the selection
def get_floor_blocks(level, box):
    ar = []
    ### Consider a way to select axis in terms of total length (Outer loop -> more important axis)
    for z in range(box.minz, box.maxz):
        for y in range(box.miny, box.maxy):
            for x in range(box.minx, box.maxx):
                if (level.blockAt(x, y, z) in walkable_blocks) and (level.blockAt(x, y + 1, z) == 0):
                    ar.append((x,y,z))
    return ar

#Will place marking tiles on the entire array of blocks (floor)
def mark_floor_blocks(level, blocks):
    for block in blocks:
        y = block[1] + 1 #Places carpet on top of the floor block
        set_block_with_level(level, block[0], y, block[2], wool_floor, wool_floor_level)

def find_road_origin(floor_blocks):
    return floor_blocks[rand.randrange(0, len(floor_blocks) / 10)] #picks a random block from the first 10% of the floor blocks

#Indicates the road origin with yellow wool
def mark_road_origin(level, origin):
    set_block_with_level(level, origin[0], origin[1] + 1, origin[2], wool_floor, 4)


def find_road_end(floor_blocks):
    return floor_blocks[rand.randrange(len(floor_blocks) - (len(floor_blocks) / 10), len(floor_blocks))] #picks a random block from the first 10% of the floor blocks

#Indicates the road end with red wool
def mark_road_end(level, end):
    set_block_with_level(level, end[0], end[1] + 1, end[2], wool_floor, 14)






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

#Calculates the block distance on the x and z axis. (Y is not counted as a step on the y axis is free)
def step_size(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[2] - point2[2]) #Y values are seen as free real estate

#Returns the path from road_origin to road_end
def build_road_astar(level, road_origin, road_end, floor_blocks):
    moves = [(1,0,0), (-1,0,0), (0,0,1), (0,0,-1), (1,1,0), (-1,1,0), (0,1,1), (0,1,-1), (1,-1,0), (-1,-1,0), (0,-1,1), (0,-1,-1)]
    open_nodes = []
    closed_nodes = []
    open_nodes.append(Path_node(None, road_origin, 0, step_size(road_origin, road_end)))
    while len(open_nodes) >= 1:
        print "starting new loop with ", len(open_nodes), " open nodes"
        node_current = get_lowest_f(open_nodes)

        if node_current.get_location() is road_end:
            print "WOW! Found the end!"
            path = []
            current = node_current
            while current is not None:
                path.append(current.get_location())
                current = current.parent
            return path
        else:
            print "Not found end yet"
            #index = floor_blocks.index(node_current.get_location())
            neighbours = []
            for move in moves:
                cl = node_current.get_location()
                nl = (cl[0] + move[0], cl[1] + move[1], cl[2] + move[2])
                if nl in floor_blocks:
                    neighbours.append(nl)

            print "block had ", len(neighbours) , " neighbours"
            for block in neighbours: #Consider generating new positions (moves) adding them to current location, then checking if that pos is in floor_blocks
                print "step size: ", step_size(node_current.get_location(), block)
                if step_size(node_current.get_location(), block) == 1:
                    new_node = Path_node(node_current, block, node_current.get_f() + step_size(node_current.get_location(), block), step_size(block, road_end))
                    if not node_in_list(new_node, open_nodes) and not node_in_list(new_node, closed_nodes):
                        open_nodes.append(new_node)

            print "Cleaning up after loop"            
            open_nodes.remove(node_current)
            closed_nodes.append(node_current)
    
def node_in_list(node, list):
    for elm in list:
        if elm.is_equal_to(node):
            return True
    return False

def get_lowest_f(open_nodes):
    lowest = open_nodes[0]
    for node in open_nodes:
        if not node.is_equal_to(lowest): #not the same node
            if node.get_f() <= lowest.get_f():
                lowest = node
    return lowest


            
def place_road(level, block_pos):
    set_block_with_level(level, block_pos[0], block_pos[1], block_pos[2], 4, 0)




#Sets block with level (i.e 171:3 for light blue wool carpet)
def set_block_with_level(level, x, y, z, blockID, blockIDLevel):
    level.setBlockAt(x, y, z, blockID)
    level.setBlockDataAt(x, y, z, blockIDLevel)

def build_tent(level, origin):
    print "Building tent"
    white_wool  = 35
    oak_fence   = 85
    red_bed     = 26
    height      = 3
    depth       = 5
    for x in range(0, height):
        for z in range(0, depth):
            tenty = (origin[1] + height) # starts from the top
            tentx = (origin[0] + (height - 1)) #height - 1 because a tent is 1 block less wide than it is tall, starts from the center
            tentz = origin[2]
            set_block_with_level(level, tentx + x, tenty - x, tentz + z, white_wool, 0) #right side
            set_block_with_level(level, tentx - x, tenty- x, tentz + z, white_wool, 0) #left side

    #Decorating tent structure
    tentx_center = origin[0] + (height - 1)
    height = height - 1
    set_block_with_level(level, tentx_center - (height - 1), origin[1] + 1, origin[2] + (depth - 1), oak_fence, 0)
    set_block_with_level(level, tentx_center + (height - 1), origin[1] + 1, origin[2] + (depth - 1), oak_fence, 0)

    set_block_with_level(level, tentx_center - (height - 1), origin[1] + 1, origin[2]  + depth + 1, 92, 0) #Cake outside
    set_block_with_level(level, tentx_center - (height - 1), origin[1] + 1, origin[2]  + int(depth/2), 62, 5) #Furnace inside

    set_block_with_level(level, tentx_center + (height - 1), origin[1] + 1, origin[2] + 1, red_bed, 2) #missing head section
    for y in range(0, height):
        set_block_with_level(level, origin[0] + (height), origin[1] + (y + 1), origin[2], oak_fence, 0)



#Directions  2==N, 3==S, 4==W, 5==E anything else == N, some blocks use directs to specify face, furnaces, chests, beds..



