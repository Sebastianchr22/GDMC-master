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
    

    #index = 0
    #for segment in segments_root.get_children():
    #    for block in segment.get_content():
    #        Builder.set_block_with_level(level, block[0], block[1], block[2], 35, index % 15)
    #    index += 1
    #Creating road within the largest segment of the partitioned space 
    #road_origin = RoadHandler.find_road_point(level, largest_segment.get_content(), (0, len(largest_segment.get_content()) / 10))
    #FloorHandler.mark_road_origin(level, road_origin)

    #road_end = RoadHandler.find_road_point(level, largest_segment.get_content(), (len(largest_segment.get_content()) - (len(largest_segment.get_content()) / 10), len(largest_segment.get_content())))
    #FloorHandler.mark_road_end(level, road_end)

    #road_blocks = RoadHandler.build_road_astar(level, road_origin, road_end, largest_segment.get_content())
    #road_blocks = RoadHandler.pave_road(level, road_blocks)
    
    #for x in range(0,10):
    #    floor_without_road = FloorHandler.get_floor_without_roads(level, largest_segment.get_content())
    #    road_blocks += RoadHandler.create_road_branch(level, road_blocks, largest_segment.get_content())
    #floor_without_road = FloorHandler.get_floor_without_roads(level, largest_segment.get_content())
    

    segment_grid = GridSeg.get_grid(largest_segment.get_content())
    index = 0
    for cube in segment_grid:
        for block in cube.get_chunk():
            Builder.set_block_with_level(level, block[0], block[1], block[2], 35, index % 15)
        index+=1

    #Build houses are return all blocks not containing a house
    #Builder.place_houses(level, road_blocks, floor_without_road)

    
            
    
    #Builder.build_farm_land(level, floor_blocks)
    #FloorHandler.mark_floor_blocks(level, floor_without_road)

    elapsed_time = time.time() - initial_time
    print "PERFORMANCE: total settlement generation time        ", elapsed_time, " seconds"
