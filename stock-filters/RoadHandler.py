import time
import random as rand
import numpy as np

#Sub-scripts
import Builder
from PathNode import Path_node

walkable_blocks = [1, 2, 3, 5, 12, 13]
road_steps = [
    (1,0), (0,1), (-1,0), (0,-1)
]


#Will generate a new branching road from the given road 
def create_road_branch(level, path, floor_blocks):
    initial_time = time.time()
    rand_point_on_road = path[rand.randrange(0, len(path))]
    rand_target_point = floor_blocks[rand.randrange(0, len(floor_blocks))]
    side_path = build_road_astar(level, rand_point_on_road, rand_target_point , floor_blocks)
    pave_road(level, side_path)
     ###For performance evaluation:
    elapsed_time = time.time() - initial_time
    print("PERFORMANCE: Creating road branch took               ", elapsed_time, " seconds")
    return side_path

#Places road path blocks along the given road path
def pave_road(level, path):
    new_road = []
    initial_time = time.time()
    for block in path:
        for step in road_steps:
            new_road.append((block[0] + step[0], block[1], block[2] + step[1]))
            Builder.set_block_with_level(level, block[0] + step[0], block[1], block[2] + step[1], Builder.get_road_block_id(), 0)
    ###For performance evaluation:
    return new_road
    elapsed_time = time.time() - initial_time
    print "PERFORMANCE: Paving road took                        ", elapsed_time, " seconds"

#Finds a random point along the road
def find_road_point(level, floor_blocks, range):
    initial_time = time.time()
    r = rand.randrange(range[0], range[1])
    bl = floor_blocks[r]
    while level.blockAt(bl[0], bl[1], bl[2]) not in walkable_blocks:
        r = rand.randrange(range[0], range[1])
        bl = floor_blocks[r]
    ###For performance evaluation:
    elapsed_time = time.time() - initial_time
    print "PERFORMANCE: Finding road point took                 ", elapsed_time, " seconds"
    return bl

#Calculates the block distance on the x and z axis. (Y is not counted as a step on the y axis is free)
def step_size(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[2] - point2[2]) #Y values are seen as free real estate

legal_steps = [ #(x,y,z)
    (1,0,0), (-1,0,0),
    (0,0,1), (0,0,-1),
    (1,1,0), (1,-1,0), 
    (-1,1,0), (-1,-1,0),
    (0,1,1), (0,1,-1), 
    (0,-1,1), (0,-1,-1),
    (0,-1,0), (0,1,0),
    #(1,0,1), (-1,0,1), (-1,0,-1), (1,0,-1), Cross moves
    #(1,1,1), (-1,1,1), (-1,1,-1), (1,1,-1),
    #(1,-1,1), (-1,-1,1), (-1,-1,-1), (1,-1,-1)
]

#Returns the path from road_origin to road_end
def build_road_astar(level, road_origin, road_end, floor_blocks):
    initial_time = time.time()
    last_node = road_origin
    open_nodes = []
    closed_nodes = []
    open_nodes.append(Path_node(None, road_origin, 0, step_size(road_origin, road_end)))
    while len(open_nodes) > 0:
        node_current = get_lowest_f(open_nodes)
        if step_size(node_current.get_location(), road_end) == 0:
            path = []
            current = node_current
            while current is not None:
                path.append(current.get_location())
                current = current.parent
            return path
        else:
            neighbours = []
            cnl = node_current.get_location()
            for step in legal_steps:
                nl = (cnl[0] + step[0], cnl[1] + step[1], cnl[2] + step[2])
                #Builder.set_block_with_level(level, cnl[0], cnl[1], cnl[2], 5, 4)
                if nl in floor_blocks:
                    neighbours.append(nl)

            for loc in neighbours: 
                new_node = Path_node(node_current, loc, node_current.get_f() + step_size(node_current.get_location(), loc), step_size(loc, road_end))
                if not in_list(new_node, open_nodes) and not in_list(new_node, closed_nodes):
                    open_nodes.append(new_node)
            last_node = node_current          
            open_nodes.remove(node_current)
            closed_nodes.append(node_current)

    print "ERROR: path could not be established to target point. Returning backup path."
    backup_path = []
    while last_node is not None:
        backup_path.append(last_node.get_location())
        last_node = last_node.parent
    #For performance evaluation:
    elapsed_time = time.time() - initial_time
    print "PERFORMANCE: Building road with A* took              ", elapsed_time, " seconds"
    return backup_path

#Used to check if a PathNode element is in the given list
def in_list(node, list):
    for elm in list:
        if elm.is_equal_to(node):
            return True
    return False

#Returns the lowest f (f=g+h) where f is the total cost of the node
def get_lowest_f(open_nodes):
    lowest = open_nodes[0]
    for node in open_nodes:
        if not node.is_equal_to(lowest): #not the same node
            if node.get_f() <= lowest.get_f():
                lowest = node
    return lowest

def get_walkable_blocks():
    return walkable_blocks