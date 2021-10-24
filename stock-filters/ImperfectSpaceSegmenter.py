import Builder
import time as time


legal_steps = [
    (1,0,0), (-1,0,0),
    (0,0,1), (0,0,-1),
    (1,1,0), (1,-1,0), 
    (-1,1,0), (-1,-1,0),
    (0,1,1), (0,1,-1), 
    (0,-1,1), (0,-1,-1),
    (0,-1,0), (0,1,0)
]

class SegmentNode():
    def __init__(self, parent, content):
        self.parent = parent
        self.content = content
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def get_children(self):
        return self.children
    
    def get_content(self):
        return self.content

#This method segments the imperfect space into a tree structure of connected blocks (segments) as children of the entirity
def get_segments(floor_without_road):
    initial_time = time.time()
    search_space = floor_without_road[:]
    root = SegmentNode(None, floor_without_road[:]) #Root represents the entire search space

    while len(search_space) > 0:
        open_blocks = [search_space.pop(0)]
        neighbouring_blocks = [open_blocks[0]]
        while len(open_blocks) > 0:
            current_block = open_blocks[0] #Getting the first block ever found (arbitrary origin)
            for step in legal_steps:
                new_block_location = (current_block[0] + step[0], current_block[1] + step[1], current_block[2] + step[2])
                if (new_block_location in search_space )and (new_block_location not in neighbouring_blocks):
                    neighbouring_blocks.append(new_block_location) #Found a new neighbour
                    search_space.remove(new_block_location) #Removed from further inspection
                    open_blocks.append(new_block_location) #Inspected next
            open_blocks.remove(current_block) #Finished all block's neighbours
        root.add_child(SegmentNode(root, neighbouring_blocks)) #No more open blocks for the segment

    elapsed_time = time.time() - initial_time
    print "PERFORMANCE: total segmentation time        ", elapsed_time, " seconds"
    
    return root

