from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
import random as rand
import time

#Sub-scripts (dependencies):
import FloorHandler #For all functions related to the flooring of the selected box (indicated by wool)
import RoadHandler #For all functions related to the road, generation, sideshoots, and point selection
import Builder
import ImperfectSpaceSegmenter as ISSeg
import SquareSegmenter as GridSeg
from Settlement import Settlement

floor_blocks = []

#Perform is the main function for an McEdit filter, meant to initiate the script functionality
def perform(level, box, options):
    initial_time = time.time()

    print "Building settlement on ", (box.maxx - box.minx), "x", (box.maxz - box.minz)


    #Finding all floor space:
    floor_blocks = FloorHandler.get_floor_blocks(level, box)
    

    #Segmenting floor space by Imperfect space partitioning (Rachability partitioning):
    #We will use the largest walkable segment out of the selection to construct the settlement
    segments_root = ISSeg.get_segments(floor_blocks)
    largest_segment = segments_root.get_children()[0]
    for child in segments_root.get_children():
        if(len(child.get_content()) > len(largest_segment.get_content())):
            largest_segment = child
    print "Largest child segment found has a size of ", len(largest_segment.get_content()), " blocks"

    #Clear trees above:
    for block in largest_segment.get_content():
        for y in range(block[1] +1, box.maxy):
            Builder.set_block_with_level(level, block[0], y, block[2], 0, 0)

    segment_grid = GridSeg.get_grid(largest_segment.get_content())
    #index = 0
    #for cube in segment_grid:
    #    for block in cube.get_chunk():
    #        Builder.set_block_with_level(level, block[0], block[1], block[2], 35, index % 15)
    #    index+=1

    #Simulation via settlers>
    
    settlement_time = time.time()
    settlemet = Settlement(10, 25, level, segment_grid, floor_blocks)
    while len(settlemet.settlers) > 0:
        settlemet.step()
    print "PERFORMANCE: Settlement simulation took ", time.time() - settlement_time, " seconds"

    #for settler in settlers:
    #    settler._get_decisions().print_decisions()

    elapsed_time = time.time() - initial_time
    print "PERFORMANCE: total settlement generation time        ", elapsed_time, " seconds"
