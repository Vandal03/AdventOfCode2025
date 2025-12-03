class JoltageFinder():

    def __init__(self):
        
        self.joltages = []
        with open("AdventOfCode2025\Day 3\joltage.txt") as content:
            self.batteryBanks = content.readlines()


    def find_joltage(self):
        
        for battery in self.batteryBanks:
            self.firstNum = 0
            self.secondNum = 0
            index = 0
            self.batteryLength = len(battery)
            for num in battery[:-1]:
                if int(num) > int(self.firstNum) and index < (self.batteryLength-2):
                    self.firstNum = num
                    self.secondNum = 0
                elif int(num) > int(self.secondNum):
                    self.secondNum = num
                index += 1
            
            joltage = self.firstNum + self.secondNum
            self.joltages.append(joltage)


    def total_joltage(self):

        totalJoltage = 0
        for joltage in self.joltages:
            totalJoltage += int(joltage)

        print(totalJoltage)









if __name__ == "__main__":
    jf = JoltageFinder()
    jf.find_joltage() 
    jf.total_joltage()