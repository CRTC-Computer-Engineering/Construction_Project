
class person():
    def __init__(self, _leg, _arm, _head, _body): # Init
        self.leg = _leg
        self.arm = _arm
        self.head = _head
        self.body = _body

    def print_data(self): # Method
        print("Number of legs: " + str(self.leg))
        print("Number of arms: " + str(self.arm))
        print("Number of heads: " + str(self.head))
        print("Number of bodies: " + str(self.body))

bob = person(2, 2, 1, 1)
jeff = person(1, 2, 1, 1)

bob.print_data()
print("sep")
jeff.print_data()
jeff = person(2, 2, 1, 1)
print("sep")
jeff.print_data()



"""f(x) = x+1
f(1) = 2

def funct(x):
    return x + 1
print(funct(1))
"""