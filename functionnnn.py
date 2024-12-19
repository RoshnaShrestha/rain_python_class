def my_function():

    print("Hello from a function")

my_function()



def sum(*args):
    result = 0 
    for number in args:
        result += number
    return result 
     
def diff(*args):
     result = 0 
     for number in args:
        result -= number
     return result 
    
def mul(*args):
    result = 1
    for number in args:
        result *= number
    return result 
def div(*args):
    result = 1
    for number in args:
        result /= number
    return result

print (sum(1,2,3))
print (diff(5,6))
print (mul(5,1))
print (div(4, 2))



def print_full_name(**kwargs):
    print(kwargs)
    print(f"My full name is {kwargs['first_name']} {kwargs['last_name']}")

print_full_name(first_name = "Roshna", last_name = "Shrestha", middles_name = "None")

def print_result(*args, **kwargs):
    print(args)
    print(kwargs)
    result = 0 
    for number in args:
        result += number
    print(f"My full name is {kwargs['first_name']} {kwargs['last_name']} and total marks ={result}")

print_result(10,20,30,40,50, first_name="Roshna", last_name ="Shrestha")