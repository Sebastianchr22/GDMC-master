class Segment(object):
    def __init__(self, chunk):
        self.chunk = chunk
        self.heightmap = []
        self.deviation = -1
        self.settlers = []
        self.is_used = False
    
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

    def add_settler(self, settler):
        if settler not in self.settlers:
            self.settlers.append(settler)

    def get_settlers(self):
        return self.settlers

    def remove_settler(self, settler):
        if settler in self.settlers:
            self.settlers.remove(settler)

    def get_segment_used(self):
        return self.is_used
    
    def use_segment(self):
        self.is_used = True