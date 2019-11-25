class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, n, *m):
        self.result= self.result+n
        for x in m:
            self.result= self.result+x
        print('result =',self.result)
        return self
    
    def subtract(self, n, *m):
        self.result= self.result-n
        for x in m:
            self.result= self.result-x
        print('result =',self.result)
        return self


    # # def add(self, n, *m):   // this code is wrong
    # #     for x in m:
    # #         self.result= self.result+n+x
    # #     return self
    
    # # def subtract(self, n, *m):
    # #     for x in m:
    # #         self.result= self.result-n-x
    # #     return self


baby = MathDojo()
baby.add(2,3,5,67)
baby.add(76,13,7,267)
baby.add(2,33,54,67,89)
baby.subtract(2,3,5,67)
baby.subtract(76,13,7,267)
baby.subtract(2,33,54,67,89)
x = baby.add(2).add(2,5,1,4,8).add(1,2,3,4).subtract(3,2,1,2,3).subtract(3,8,2,3).subtract(3,4,2,1).result
print(x)