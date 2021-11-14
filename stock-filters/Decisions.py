from Decision import Decision

class Decisions:
    def __init__(self) -> None:
        self.root = [Decision("I'm alive!", None, None)]

    def new_decision(self, decision):
        self.root.append(decision)

    def get_decision_num(self) -> int:
        return len(self.root)

    def get_decision_at(self, index : int) -> Decision:
        return self.root[index]

    def print_decisions(self) -> None:
        t = ""
        for dec in self.root:
            text = t + dec.get_text() + " -> "
            t = text
        print(text)