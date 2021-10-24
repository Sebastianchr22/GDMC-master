import time as time

legal_moves_from_origin = [
    (1,0,0), (-1,0,0),
    (0,0,1), (0,0,-1),
    (1,1,0), (1,-1,0), 
    (-1,1,0), (-1,-1,0),
    (0,1,1), (0,1,-1), 
    (0,-1,1), (0,-1,-1),
    (0,-1,0), (0,1,0)
]

open_directions = []


class Square:
    def __init__(self, parent, origin, content):
        self.parent = parent
        self.origin = origin
        self.content = content
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def add_to_content(self, block):
        self.content.append(block)
    
    def get_children(self):
        return self.children
    
    def get_content(self):
        return self.content
    
    def get_origin(self):
        return self.origin


#Assumes the search space is walkable and already segmented using the ImperfectSpaceSegmenter.
def get_segments(segments):
    initial_time = time.time()
    search_space = segments[:] #Copies the segments as search space
    root = Square(None, search_space[0], search_space)

    for segment in search_space:
        open_blocks = segment.get_content() #Getting all blocks contained in the segmented walkable space
        for block in open_blocks: #Iterating over each block in the segment
            neighbours = []
            for step in legal_moves_from_origin:
                next_block = (block[0] + step[0], block[1] + step[1], block[2] + step[2])
                if next_block in open_blocks:
                    #Neighbour block found  in the set of blocks
                    open_directions.append(step)
                    neighbours.append(next_block)
                    open_blocks.remove(next_block)
            #Now found all directions in which to travel from the origin
            if len(open_directions) >= 1: 
                while(len(open_directions) > 0):
                    for step in open_directions:
                        next_block = (block[0] + step[0], block[1] + step[1], block[2] + step[2])
                        if next_block in open_blocks:
                            neighbours.append(next_block)
                            open_blocks.remove(next_block)
                        else:
                            open_directions.remove(step)
                #if len(neighbours) > 2:
                root.add_child(Square(root, block, neighbours))


    elapsed_time = time.time() - initial_time
    print("PERFORMANCE: total square segmentation time        ", elapsed_time, " seconds")
    return root
