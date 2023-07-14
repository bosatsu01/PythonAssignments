import math

class MyMathModule:
    def _init_(self, number):
        self.number = number
    
    def sqr(self):
        return self.number ** 2
    
    def sqr_root(self):
        return math.sqrt(self.number)
    
    def fact(self):
        return math.factorial(self.number)
    
    def logarithm(self):
        return math.log(self.number)
    
   
    
class MyException(Exception):
    def init(self, message):
        self.message = message

    def msg(self):
        return self.message