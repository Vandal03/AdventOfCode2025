import csv


class invalid_id_checker():
    def __init__(self):
        with open("Day 2/ranges.txt") as content:
            line = content.readline()
            self.ids = line.split(",")
            self.toCount = []
        
    def run_check(self):
        for id in self.ids:
            minMax = id.split("-")
            min = minMax[0]
            max = minMax[1]
            i = int(minMax[0])
            while i <= int(max):
                length = len(str(i))
                if length % 2 == 0:
                    half = int(length/2)
                    halfOne = str(i)[0:half]
                    halfTwo = str(i)[half:length]
                    if halfOne == halfTwo:
                        self.toCount.append(i)
                        print(i)
                    i += 1
                    
                else:
                    i+=1

        finalCount = 0
        for id in self.toCount:
            finalCount += id
        print(f"Final Count: {finalCount}")
            



if __name__ == "__main__":
    checker = invalid_id_checker()
    checker.run_check()




