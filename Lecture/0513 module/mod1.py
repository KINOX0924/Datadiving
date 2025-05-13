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