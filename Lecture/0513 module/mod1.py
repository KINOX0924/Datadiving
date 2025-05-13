"""
def add(x , y) :
    return x + y

def sub(x , y) :
    return x - y

class Person :
    def __init__(self , name = "" , age = 0) :
        self.name = name
        self.age  = age
        
    def print(self) :
        print(f"name = {self.name} | age = {self.age}")

if __name__ == "__main__" :
    print(add(3,4))
    print(sub(3,4))

    p1 = Person("강태풍" , 12)
    p1.print()
"""

def isEven(args) :
    if args % 2 == 0 :
        return True
    return False

def toUpper(char) :
    return char.upper()