print("Hello world")

if 5 > 2:
    print("5 is grater")    #tyo print same line ma hunu parxa tala rw mathi 
    print("2 is smaller")

x = 5
y = "Hello World"
print(id(x)) #memory ko location bataiidinxa
print(y)
print(type(x))
print(type(y)) #type check garxa
# mero python class notes 12/12


mail = "this is a mail"

"""
this is a mail
 yo 3 ota diyo vani ya bhitra j lekhda ni print hudaiina 
yeslaii multiline string vanxa
"""

print(mail)  

#type change gareko = type casting 
d = 7.5
print(type(d))


d = int(d)
print(type(d))


a = 3
b = "2"

if a > int(b):
    print("a is greater")

a = 1
A = 4 #yo a rw A different variables ho 

age = 8
Age = 8


myObject = 5 #Camel Case
MyObject = 5 #pascal case class banauda use hunxa
my_object = 5 # Snake case variable banauda use hunxa

#Many Values to Multiple Variables
x, y, z = "Orange","Banana", "Mango"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Kiwi"
print(x)
print(y)
print(z)


#Unpack a Collection

fruits = ["Orange","Banana", "Mango"]
x,y,z = fruits
print(x)
print(y)
print(z)


#Boolean Values
a = True
b = False
print(a and b)  #hami ley and or not pani use garna milxa
print(a or b)
print(not b)


boy_age = 19
boy_country = "Nepal"

if boy_age > 18 and boy_country == "Nepal":
    print("Boy can give licence exam in Nepal")

print("...........................................................................")
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



