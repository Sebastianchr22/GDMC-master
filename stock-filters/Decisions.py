from Decision import Decision

class Decisions:
    def __init__(self):
        self.root = Decision("I'm alive!", None, None)
        self.latest_decision = self.root

    def new_decision(self, decision):
        self.latest_decision.add_next_decision(decision)
        self.latest_decision = decision

    def get_decision_num(self):
        dec = self.root
        i = 0
        while dec != None:
            i += 1
            dec = dec.get_next_decision()
        return i

    def get_decision_at(self, index):
        dec = self.root
        i = 0
        while dec != None:
            i += 1
            if i == index:
                return dec
            dec = dec.get_next_decision()

    def print_decisions(self):
        t = ""
        dec = self.root
        while dec != None:
            text = t + dec.get_text() + " -> "
            t = text
            dec = dec.get_next_decision()
        print(text)