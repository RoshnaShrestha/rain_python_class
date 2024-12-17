
first_number = float (input ("Enter your first number : "))
second_number = float (input ("Enter your second number :"))
 
#first_number = int(first_number)

print("Addition = ", first_number + second_number)

print("For Subtraction")
first_number = float (input ("Enter your first number : "))
second_number = float (input ("Enter your second number :"))

print("Subtraction = ", first_number - second_number)

print("For Multiplication")
first_number = float (input ("Enter your first number : "))
second_number = float (input ("Enter your second number :"))

print("Multiplication = ", first_number * second_number)
print("divison = ", first_number / second_number)
print("Modulus= ", first_number % second_number)
print("	Exponentiation = ", first_number ** second_number)
print("	Floor division= ", first_number // second_number)


first_number = float (input ("Enter your first number : "))
second_number = float (input ("Enter your second number :"))
user_choice = input(  
    """ 
                    Please choose your option
                    +for Addition 
                    - for Subtraction
                    * for Multiplication
                    % for division
                    
                
                    """ )

if user_choice == "+":
    print("Addition = ", first_number + second_number)
elif user_choice == "-":
    print("Subtraction = ", first_number - second_number)
else:
    print("Invalid option ")



