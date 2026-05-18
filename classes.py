class Difference:
    def __init__(self, a):
        self.__elements = a
   
        
    def computeDifference(self):
        self.maximumDifference=0
        for i in self.__elements:
            diff=0
            for j in self.__elements:
                diff= i - j
                if diff<0:
                    diff=-diff
                    
                if diff > self.maximumDifference:
                    self.maximumDifference=diff


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
