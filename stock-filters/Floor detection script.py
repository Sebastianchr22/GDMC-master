from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
import random as rand

floor_blocks = []
walkable_blocks = [1, 2, 3, 4, 5, 12, 13]
wool_floor= 171
wool_floor_level = 0
water_block_id = 9

def perform(level, box, options):
    floor_blocks = get_floor_blocks(level, box)
    #uf.setBlock(level, (1,0), x, y, z)
    #print "Floor blocks found: " , len(floor_blocks)

    #mark_floor_blocks(level, floor_blocks)

    road_origin = find_road_point(level, floor_blocks, (0, len(floor_blocks) / 10))
    mark_road_origin(level, road_origin)

    road_end = find_road_point(level, floor_blocks, (len(floor_blocks) - (len(floor_blocks) / 10), len(floor_blocks)))
    mark_road_end(level, road_end)

    main_road = build_road_astar(level, road_origin, road_end, floor_blocks)
    pave_road(level, main_road)
    
    for x in range(0,8):
        floor_blocks = get_floor_blocks(level, box)
        create_road_branch(level, main_road, floor_blocks)
    #build_tent(level, floor_blocks[0])

def create_road_branch(level, path, floor_blocks):
    rand_point_on_road = path[rand.randrange(0, len(path))]
    rand_target_point = floor_blocks[rand.randrange(0, len(floor_blocks))]
    side_path = build_road_astar(level, rand_point_on_road, rand_target_point , floor_blocks)
    pave_road(level, side_path)

def pave_road(level, path):
    for block in path:
        set_block_with_level(level, block[0], block[1], block[2], 4, 0)

#Will return an array of tuples representing all blocks that are walkable from the selection
def get_floor_blocks(level, box):
    ar = []
    ### Consider a way to select axis in terms of total length (Outer loop -> more important axis)
    for z in range(box.minz, box.maxz):
        for y in range(box.miny, box.maxy):
            for x in range(box.minx, box.maxx):
                block = level.blockAt(x, y, z)
                if block in walkable_blocks and level.blockAt(x, y + 1, z) == 0:
                    ar.append((x,y,z))

    return ar

#Will place marking tiles on the entire array of blocks (floor)
def mark_floor_blocks(level, blocks):
    for block in blocks:
        y = block[1] + 1 #Places carpet on top of the floor block
        set_block_with_level(level, block[0], y, block[2], wool_floor, wool_floor_level)

def find_road_point(level, floor_blocks, range):
    r = rand.randrange(range[0], range[1])
    bl = floor_blocks[r]
    while level.blockAt(bl[0], bl[1], bl[2]) not in walkable_blocks:
        r = rand.randrange(range[0], range[1])
        bl = floor_blocks[r]
    return bl

#Indicates the road origin with yellow wool
def mark_road_origin(level, origin):
    set_block_with_level(level, origin[0], origin[1] + 1, origin[2], wool_floor, 4)

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
    last_node = road_origin
    open_nodes = []
    closed_nodes = []
    open_nodes.append(Path_node(None, road_origin, 0, step_size(road_origin, road_end)))
    while len(open_nodes) > 0:
        node_current = get_lowest_f(open_nodes)
        #print "Current f = ", node_current.get_f()
        if node_current.get_location() is road_end:
            path = []
            current = node_current
            while current is not None:
                path.append(current.get_location())
                current = current.parent
            return path
        else:
            #index = floor_blocks.index(node_current.get_location())
            for blocks in floor_blocks: #Consider generating new positions (moves) adding them to current location, then checking if that pos is in floor_blocks
                #print "step size: ", step_size(node_current.get_location(), blocks)
                if step_size(node_current.get_location(), blocks) == 1:
                    new_node = Path_node(node_current, blocks, node_current.get_f() + step_size(node_current.get_location(), blocks), step_size(blocks, road_end))
                    if not in_list(new_node, open_nodes) and not in_list(new_node, closed_nodes):
                        open_nodes.append(new_node)
            last_node = node_current          
            open_nodes.remove(node_current)
            closed_nodes.append(node_current)
    print "Error: path could not be established to target point. Returning backup path."
    backup_path = []
    while last_node is not None:
        backup_path.append(last_node.get_location())
        last_node = last_node.parent
    return backup_path
    
def in_list(node, list):
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



