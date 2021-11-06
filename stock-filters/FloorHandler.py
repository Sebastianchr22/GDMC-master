from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
import random as rand
import time

#Sub-scripts  (dependencies)
import Builder

floor_blocks = []
walkable_blocks = [1, 2, 3, 5, 12, 13]
plants = [6, 31, 32, 37, 38, 39, 40, 175]

wool_floor = Builder.get_floor_block_id()


def get_floor_without_roads(level, floor_blocks):
    initial_time = time.time()
    ar = []
    for block in floor_blocks:
        if level.blockAt(block[0], block[1], block[2]) != Builder.get_road_block_id():
            ar.append(block)
    ###For performance evaluation:
    elapsed_time = time.time() - initial_time
    print "PERFORMANCE: Getting floor blocks without road took  ", elapsed_time, " seconds"
    return ar

#Will return an array of tuples representing all blocks that are walkable from the selection
def get_floor_blocks(level, box):
    initial_time = time.time()
    ar = []
    ### Consider a way to select axis in terms of total length (Outer loop -> more important axis)
    for x in range(box.minx, box.maxx):
        for z in range(box.minz, box.maxz):
            for y in range(box.maxy, box.miny, -1):
                block = level.blockAt(x, y, z)
                block_above = level.blockAt(x, y + 1, z)
                if block in walkable_blocks and (block_above == 0 or block_above in plants):
                    ar.append((x,y,z))
                    break
    
    ###For performance evaluation:
    elapsed_time = time.time() - initial_time
    print "PERFORMANCE: Getting floor blocks took               ", elapsed_time, " seconds"
    return ar

#Will place marking tiles on the entire array of blocks (floor)
def mark_floor_blocks(level, blocks):
    initial_time = time.time()
    for block in blocks:
        y = block[1] + 1 #Places carpet on top of the floor block
        Builder.set_block_with_level(level, block[0], y, block[2], wool_floor, 10)
    ###For performance evaluation:
    elapsed_time = time.time() - initial_time
    print "PERFORMANCE: Marking floor blocks took               ", elapsed_time, " seconds"

#Indicates the road origin with yellow wool
def mark_road_origin(level, origin):
    Builder.set_block_with_level(level, origin[0], origin[1] + 1, origin[2], wool_floor, 4)

#Indicates the road end with red wool
def mark_road_end(level, end):
    Builder.set_block_with_level(level, end[0], end[1] + 1, end[2], wool_floor, 14)



