class JoltageFinder():

    def __init__(self):
        
        self.joltages = []
        with open("AdventOfCode2025\Day 3\joltage.txt") as content:
            self.batteryBanks = content.readlines()


    def find_joltage(self):
        
        for battery in self.batteryBanks:
            self.joltageArray = []
            self.batteryRemaining = len(battery) - 1 
            for num in battery[:-1]:
                match len(self.joltageArray):
                    case 0:
                       self.joltageArray.append(num)
                    case 1|2|3|4|5|6|7|8|9|10|11|12:
                       self.check_array(num)

                self.batteryRemaining -= 1

        print(self.joltageArray)



    def check_array(self, num):
        index = 0
        joltageArrayLength = len(self.joltageArray)
        for value in self.joltageArray:
            #check length of array vs what's remaining in battery values
            if joltageArrayLength % self.batteryRemaining == 0:
                self.joltageArray.append(num)
                break
            elif int(num) > int(value):
                self.joltageArray[index] = num
                self.joltageArray = self.joltageArray[0:index + 1]
                break
            elif (index + 1) == joltageArrayLength:
                self.joltageArray.append(num)
                
            
            index += 1
            
                












if __name__ == "__main__":
    jf = JoltageFinder()
    jf.find_joltage() 
 