class Segment(object):
    def __init__(self, chunk):
        self.chunk = chunk
        self.heightmap = []
        self.deviation = -1
    
    def get_chunk(self):
        return self.chunk

    def get_heightmap(self):
        if len(self.heightmap) <= 0:
            origin = self.chunk[0]
            for block in self.chunk:
                self.heightmap .append(block[1] - origin[1])
        return self.heightmap 
    
    def get_deviations(self):
        if self.deviation <= 0:
            for height in self.heightmap:
                self.deviation += abs(height)
        return self.deviation

