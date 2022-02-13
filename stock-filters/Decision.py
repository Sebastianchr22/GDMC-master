class Decision:
    def __init__(self, text, impulse, considerations):
        self.text = text
        self.impulse = impulse
        self.considerations = considerations
        self.next_decision = None
    
    def get_text(self):
        return self.text
    
    def get_considerations(self):
        return self.considerations
    
    def get_impulse(self):
        return self.impulse

    def add_next_decision(self, decision):
        self.next_decision = decision

    def get_next_decision(self):
        return self.next_decision
