class Decision:
    def __init__(self, text, impulse, considerations):
        self.text = text
        self.impulse = impulse
        self.considerations = considerations
    
    def get_text(self):
        return self.text
    
    def get_considerations(self):
        return self.considerations
    
    def get_impulse(self):
        return self.impulse
