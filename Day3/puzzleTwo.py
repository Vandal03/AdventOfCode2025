class JoltageFinder():

    def __init__(self):
        
        self.joltages = []
        with open("AdventOfCode2025/Day3/joltage.txt") as content:
            self.batteryBanks = content.readlines()


    def find_joltage(self):
        for battery in self.batteryBanks:
            self.joltageArray = []
            self.batteryLengthRemaining = len(battery) - 1
            while self.batteryLengthRemaining > 12:
                for num in battery[:-1]:
                    index = 0
                    self.batteryLengthRemaining -= 1
                    if len(self.joltageArray) == 0:
                        self.joltageArray.append(num)
                    else:
                        for value in self.joltageArray:
                            
                            if int(num) > int(value):
                                self.joltageArray[index] = num
                                self.joltageArray = self.joltageArray[0:index + 1]
                                break
                            index += 1
            ## if 12 > index 0
            ## if 11 > index 1
            index = -13
            for value in self.joltageArray:
                if int(value) < int(battery[index]):
                    


            
            
            
            
            


if __name__ == "__main__":
    jf = JoltageFinder()
    jf.find_joltage() 
 