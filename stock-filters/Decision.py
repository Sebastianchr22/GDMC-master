class Decision:
    def __init__(self, text, impulse, considerations) -> None:
        self.text = text
        self.impulse = impulse
        self.considerations = considerations
    
    def get_text(self) -> str:
        return self.text
    
    def get_considerations(self) -> str:
        return self.considerations
    
    def get_impulse(self) -> int:
        return self.impulse
