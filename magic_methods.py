#Trying out magic methods in Python

class Car:

    #defining __init__ method ; method used to instantiaze a class
    def __init__(self,string):
        self.string = string
        pass
    
    #repr method ; method that returns a readable representaion of an object
    def __repr__(self):
        return f"Car('{self.string}')"

    # str method ; used to use class instances in print statements
    def __str__(self):
        return f"The car name is {self.string} str"

    # len method ; calculates lenght of a variable
    def __len__(self):
        return len(self.string)

    #class method; makes classes callable
    def __call__(self):
        return self.string

    
#instantiating class object    
c = Car('Honda')

#printing to check outputs of different magic methods
print(repr(c)) 
print(str(c))
print('The length of the car name is:', len(c))
print(c())