# Question no 1 # Input a number-> Double it -> Add 10-> halve it ->  Subtract Original-> Output -> 5
while True:
    print("................Input a number -> Double it -> Add 10-> halve it ->  Subtract Original-> Output -> 5..............")
    number =  int (input ("Enter your number :"))
    double = number * 2
    print("The double number is : " , double )
    y = double + 10
    print("Adding 10 is: " , y)
    z = y/2
    print("Half of y is: " , z)
    a = z - number
    print("Subracting the original : " , a)
    user_choice = input ("""
                         Do you want to continue ? yes or no
                         """)
    if user_choice.lower() == "no":
        break

#Q.n 2 # Temperature (Celsius to fahrenheit) length(meters into kilometers, feet into inches) currency(using hardcoded exchange rates).
print("...........................Temperature (Celsius to fahrenheit)....................................")
cel = float(input("Enter the Celsius : " ))
fah= (cel*9/5)+32
print("The temperature is : " , fah)

print(".....length(meters into kilometers).......")
meters = int (input ("Enter your Meters : "))
kilometers = meters/1000 
print("Your length in kilometers is : " , kilometers)


print("........... feet into inches...............")
feet = int(input( "Enter your feet:  "))
inches = int(feet*12)
print("Your length in inches is : ", inches)

print ("............................currency(using hardcoded exchange rates)......................................")

Dollar = float(input("Enter your currency of USA : "))
Rupees = Dollar * 135.746
print("Your amount in rupees", Rupees)

#next process
while True:
    user_choice = input ( """
                     1. KM to Miles
                     2. Miles to KM
                     3. Centimeter to Inch
                     4. Inch to Centimeter
                         """)
    if user_choice == "i":
        user_input = float (input("Enter KM"))
        result = user_input * 0.621371
        print(f"{user_input} KM = {result} Miles")
        
    elif user_choice == "2":
        user_input = float (input("Enter Miles"))
        result = user_input * 1.60934
        print(f"{user_input} Miles = {result} KM")

    elif user_choice == "3":
        user_input = float (input("Enter Centimeter"))
        result = user_input * 0.393701
        print(f"{user_input} Centimeter = {result} Inch")

    elif user_choice == "4":
        user_input = float (input("Enter Inch"))
        result = user_input * 2.54
        print(f"{user_input} Inch = {result} Centimeter")

    else: 
        print("Invalid Input")
    user_choice = input ("""
                         Do you want to continue ? yes or no
                         """)
    if user_choice.lower() == "no":
        break
       

# Financial Mini-Apps
# Q.N 3 Create a program to calculate simple interest or compound interest.

print(".......................................Simple Interest................................................")
Principle = float(input("Enter the principle : "))
Time = float(input("Enter Your time : "))
Rate = float (input("Enter your rate : "))
SimpleInterest = (Principle*Time*Rate)/ 100
print("Value of SimpleInterset is : " ,SimpleInterest)


print("...........Compound Interest...................")
Principle = float(input("Enter your principle : "))
Rate = float (input("Enter your rate in % : ")) / 100
Number = int(input("Enter the Number of Times Interest Compounded per Year : "))
Time = float(input ("Enter your time : "))
Amount = Principle  * (1 + Rate / Number) ** (Number * Time)
CompoundInterest = Amount - Principle
print ("Total Amount is : ", Amount )
print("Your CompoundInterest is : ", CompoundInterest)


# Geometry Calculator
#Calculate the area and perimeter of shapes (rectangle, circle, triangle).

print("............................................Area and perimeter of Rectangle..................................................")

Length =float (input ("Enter your Length : "))
Width = float (input("Enter your Width : "))
Area = Length * Width
print("Area of a rectangle is : " , Area)
Perimeter = 2 * (Length + Width )
print("Perimeter of a rectangle is : ", Perimeter)

print(".....................................Area and perimeter of Circle...................................................")

radius = float(input("Enter your radius : "))
pie = 3.14
Area_Circle = pie * radius * radius 
Perimeter_Circle = 2 * pie* radius 
print("Area of Circle is : ", Area_Circle)
print("Perimeter of Circle is : ", Perimeter_Circle)


print(".......................................Area and perimeter of tringle.....................................")

side_1 = int (input("Enter your Side_1 :" ))
side_2 = int (input("Enter your Side_2 :" ))
side_3 = int (input("Enter your Side_3 :" ))
height= int (input ("Enter the height: "))
Area_Tringle = (height*side_1) * 1/2
Perimeter_Tringle = side_1 + side_2 + side_3 
print("Area of Tringle is : ", Area_Tringle)
print("Perimeter of Tringle is : ", Perimeter_Tringle)



#Next process
print("Calculate the area and perimeter of shapes (rectangle, circle, triangle).")
user_choice == input ( """
                      1.Circle
                      2.Rectangle
                      3.Triangle
                      """ 
                      )
if user_choice == "1":
    user_radius = float(input("Enter Radius : "))
    result_area = 3.14 * user_radius ** 2
    result_perimeter = 2 * 3.14 * user_radius 
    print(f"Area = {result_area}")
    print(f"Perimeter = {result_perimeter}")

elif user_choice == "2":
    user_length = float(input("Enter length : "))
    user_width= float(input("Enter Width : "))
    result_area = user_length * user_width
    result_perimeter = 2 * (user_length + user_width)
    print(f"Area = {result_area}")
    print(f"Perimeter = {result_perimeter}")

elif user_choice == "3":
    user_base = float(input("Enter Base : "))
    user_height= float(input("Enter heigth : "))
    result_area = 0.5 * user_base * user_height
    result_perimeter = user_base + user_height
    print(f"Area = {result_area}")
    print(f"Perimeter = {result_perimeter}")

else :
    print("Invalid Input")




"""
Number Properties Checker
Goal: Teach conditions and arithmetic together.
Activity:
Check if a number is even/odd.
Determine if a number is prime.
Find whether a number is a multiple of another number.

"""

print("........................................Check if a number is even/odd......................................")

number_1 = int (input("Enter your number : "))
if number_1 % 2 == 0:
    print("Number is even ")
else :
    print ("Number is odd")


print("....................................Determine if a number is prime..........................................")
number = int (input ("Enter your number : "))
for i in range (2, number):
    if number % i == 0:
        print(" Not Prime")
        break 
else:
    print("Prime")

print(".........................................Find whether a number is a multiple of another number......................................")

num_1 = int(input("Enter a first number : "))
num_2 = int(input("Enter your Second number : "))

if num_1 % num_2 == 0:
    print("The number is divisible")
else:
    print("The number is not divisible")


#Check number is square number 
user_number = int (input("Enter number : "))
for i in range (1 , user_number):
    if i * i == user_number:
        print (f"{user_number} is a square number ")
        break 
else:
    print(f"{user_number} is not a square number ")



