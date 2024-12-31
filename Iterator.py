# Example 1: Iterator

"""
class MyIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index>= len(self.data):
            raise StopIteration
        print(f"Getting index: {self.index}")
        value = self.data[self.index]
        self.index += 1
        return value
#Example 2: Using Iterator
my_list = [1,2,3,4,5]
my_iter = MyIterator(my_list)

for num in my_iter:
    print(num) #output: 1 2 3 4 5 

#Abstract:
.................................yo code laii run garna ko lagi tyo from abc wala kine rw abstractmethod hataiidini........
aani run garda none aako cahi tya hami ley kaii return naii nagaraya vayara aako


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        print("Vehicle is driving")
        #pass
def new_fn(self):
    print("My new fn")

class Car(Vehicle):
    pass
# def drice(self):
#return "Car is driving"

#using abstraction
car = Car()
print(car.drive()) #Output:Car is driving

# veh = vehicle()
#print(veh.drive()) #Access abstract method
"""

#Example Encapsulation

class BankAccount:
    def __init__(self,name):
        self._balance = 0
        self.name = name

    def deposite(self,amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance 
    
    def __str__(self):
        return f"Name: {self.name} and Balance = Hidden"
    
#Example Using encapsulation
roshna = BankAccount("Roshna")
roshna.deposite(10000)
print(roshna)
print(roshna.get_balance)
roshna.withdraw(100)
roshna.deposite(400)
roshna.withdraw(900)
print(roshna.get_balance())




