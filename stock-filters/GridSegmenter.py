import time

chunk_template = [ #(x,z) y is unimportant, and dealt with later
    [(0,0), (1,0), (2,0), (3,0), (4,0)],
    [(0,1), (1,1), (2,1), (3,1), (4,1)],
    [(0,2), (1,2), (2,2), (3,2), (4,2)],
    [(0,3), (1,3), (2,3), (3,3), (4,3)],
    [(0,4), (1,4), (2,4), (3,4), (4,4)],
]

blocks_in_chunk = 5*5

#This will return a 2D grid of chunks, where chucks are rectagles of traversable blocks
def get_grid(floor_blocks):
    initial_time = time.time()
    grid = []
    space = floor_blocks[:]
    xz_space = make_xz_copy(space[:])

    while len(space) > 0:
        block = space[0]
        xz_block = (block[0], block[2])
        chunk = []

        for row in chunk_template:
            for cell in row:
                nb = (cell[0] + xz_block[0], cell[1] + xz_block[1])
                if nb in xz_space:
                    chunk.append((nb[0], space[xz_space.index(nb)][1], nb[1]))

        if len(chunk) == blocks_in_chunk:
            heightmap = produce_heightmap(chunk)
            deviations = get_deviations(heightmap)
            print "Chunk deviates with ", deviations, " block on average around its center block"
            #if deviations <= 25:
            grid.append(chunk)
            for x in chunk:
                space.remove(x)
                xz_space.remove((x[0], x[2]))
            #else:
            #    space.pop(0)
            #    xz_space.remove(xz_block)
        else:
            space.remove(block)
            xz_space.remove(xz_block)

    #For performance evaluation:
    elapsed_time = time.time() - initial_time
    print "PERFORMANCE: Finding grid cells of size", blocks_in_chunk, " took ", elapsed_time, " seconds"

    return grid

#Creates a 1:1 copy of the original 3D space, by disregards the y-axis (can be found by index in the original)
def make_xz_copy(list):
    copy = []
    for elem in list:
        copy.append((elem[0], elem[2]))
    return copy

def produce_heightmap(chunk):
    total = len(chunk)
    y_sum = 0
    for block in chunk:
        y_sum += block[1]
    center = chunk[int(len(chunk) / 2)]
    hm = []
    for block in chunk:
        hm.append(block[1] - center[1])
    return hm

def get_deviations(heightmap):
    dev = 0
    for height in heightmap:
        dev += abs(height)
    return dev
