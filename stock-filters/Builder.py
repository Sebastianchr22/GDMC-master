from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
import numpy as np
import random as rand
from CubeHouse import CubeHouse
from TentHouse import TentHouse
from TestHouse import TestHouse
from CenterStructure import CenterStructure

wool_floor          = 171
water_block         = 9
cobblestone         = 4
oak_wood_plants     = 5
glass_block         = 20
white_wool          = 35
oak_fence           = 85
red_bed             = 26
furnace             = 62
cake                = 92

walkable_blocks = [1, 2, 3, 5, 12, 13]
directions = {0: "North", 1: "East", 2: "South", 3: "West"}

#Sets block with level (i.e 171:3 for light blue wool carpet)
def set_block_with_level(level, x, y, z, blockID, blockIDLevel):
    if blockID != -1:
        level.setBlockAt(x, y, z, blockID)
        level.setBlockDataAt(x, y, z, blockIDLevel)

#Will find the center of the city and build the center structure.
def build_settlement_center(level, road_blocks, floor_blocks):
    center_struct = CenterStructure()
    loc = road_blocks[int(len(road_blocks) / 2)]
    build_structure(level, loc[0], loc[1], loc[2], center_struct, 0)

#Follow the road to place houses along it,
#This will use the image scanning approach (from computer vision) to match the pattern of a building to the surrounding blocks
def place_houses(level, road_blocks, floor_blocks):
    houses = [CubeHouse(), TentHouse()]
    #houses = [TestHouse()]
    #houses = [TentHouse()]
    #houses = [CubeHouse()]
    for block in road_blocks:
        for direction in range(0, 4): #1:North, 2:East, 3:South, 4:West
            for house in houses:
                pt = house.get_patterns()[direction]
                #Looks for floor at or underneath the (x,z) coordinates of the structure.
                struct_loc = [(elem[0] + block[0], elem[1] + block[2]) for elem in pt] #Represents all blocks that must be floor blocks to match the pattern of the structure from the point block_loc
                if all_blocks_present(struct_loc, floor_blocks):
                    orgs = house.get_origins()[direction]
                    origin_loc = (orgs[0] + block[0], orgs[1] + block[2])
                    build_structure(level, origin_loc[0], block[1] + 1, origin_loc[1], house, direction)
                    
                    #set_block_with_level(level, origin_loc[0], block[1] + 7,origin_loc[1], 22, 0)
                    
                    #Remove all used blocks from floor_blocks (avoid overlap)
                    #heightmap = get_heightmap(block[1], struct_loc, floor_blocks)
                    floor_blocks = remove_xz_similar_elements(struct_loc, floor_blocks)
                    build_support_from(level, block[1], struct_loc)
    

#Removes all similar (x,z) elements from A that may be found in B
#Assumes A is [(x,z), ...] and B is [(x,y,z), ...]
def remove_xz_similar_elements(a, b):
    ar = []
    b_points = get_xz_of(b)
    for index in range(0, len(b)):
        if b_points[index] not in a:
            #Similar elements
            ar.append(b[index])
    return ar

#Returns true if all blocks are present in the provided set
def all_blocks_present(blocks, set):
    xz_blocks = get_xz_of(set)
    for block in blocks:
        if block not in xz_blocks:
            return False
    return True

#Returns a list of only (x,z) coords of a list of locations
def get_xz_of(list):
    ar = []
    for elm in list:
        ar.append((elm[0], elm[2]))
    return ar

#Builds a structure from its blueprint on the origin coordinates.
def build_structure(level, originx, originy, originz, struct, direction):
    bp = struct.get_blueprints()[direction]
    directions = ["North", "East", "South", "West"]
    print("Building a structure of sizes y=", len(bp), " x=", len(bp[0]), " z=", len(bp[0][0]), " facing ", directions[direction])
    for y in range(0, len(bp)):
        for x in range(0, len(bp[y])):
            for z in range(0, len(bp[y][x])):
                #Analyze the box inwhich to build the house, to find the floor block with the maxy and the one with the miny
                #This is to properly generate a platform onwhich the house is built
                set_block_with_level(level, originx + x, originy + y, originz + z, (bp[y][x][z])[0], (bp[y][x][z])[1])    

def build_support_from(level, inity, structure_location):
    for loc in structure_location:
        height = 0
        while level.blockAt(loc[0], inity - height, loc[1]) not in walkable_blocks:
            set_block_with_level(level, loc[0], inity - height, loc[1], cobblestone, 0)
            height += 1

def build_farm_land(level, floor_blocks):
    for block in floor_blocks:
        if level.blockAt(block[0], block[1], block[2]) == 2:
            set_block_with_level(level, block[0], block[1], block[2], 3, 1)
            set_block_with_level(level, block[0], block[1] + 1, block[2], 59, 7)


#Getters for building materials:
def get_road_block_id():
    return cobblestone

def get_floor_block_id():
    return wool_floor

def get_water_block_id():
    return water_block

def get_white_wool_block_id():
    return white_wool

def get_oak_fence_block_id():
    return oak_fence

def get_bed_block_id():
    return red_bed

def get_cake_block_id():
    return cake

def get_furnace_block_id():
    return furnace

def get_oak_wood_block_id():
    return oak_wood_plants

def get_glass_block_id():
    return glass_block