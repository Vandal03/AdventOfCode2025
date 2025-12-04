class Rolls():
    def __init__(self):
        
        with open("AdventOfCode2025\Day 4\input.txt") as content:
            rollLayout = content.readlines()
            self.layout = []
            for line in rollLayout:
                row = []
                for spot in line:
                    row.append(spot)
                self.layout.append(row)

    def checkAdjacent():
        pass

if __name__ == "__main__":
    rollFinder = Rolls()
    rollFinder.checkAdjacent()