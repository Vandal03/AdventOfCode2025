class combination:
    def __init__(self):
        self.zero_count = 0
        self.starting_pos = 50



    def update_dial(self, turn):
        self.turnLen = len(turn)
        self.direction = turn[0]
        self.clicks = int(turn[1:(self.turnLen-1)])
        if self.direction == "L":
            self.click = 0
            while self.click < self.clicks:
                if self.starting_pos == 99:
                    self.starting_pos = 0
                    self.click += 1
                else:
                    self.starting_pos = self.starting_pos + 1
                    self.click += 1
                    
                if self.starting_pos == 0:
                    self.zero_count += 1
        else:
            self.click = 0
            while self.click < self.clicks:
                if self.starting_pos == 0:
                    self.starting_pos = 99
                    self.click += 1
                else:
                    self.starting_pos = self.starting_pos - 1
                    self.click +=1

                if self.starting_pos == 0:
                    self.zero_count += 1
        


if __name__ == "__main__":
    
    comb = combination()
    
    with open("turns.txt") as content:
        turns = content.readlines()
        for turn in turns:
            comb.update_dial(turn)

    print(comb.zero_count)
                
