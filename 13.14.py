"""

x = "Whats your name?"
print(x)



for x in "banana":
  print(x)




a= "Hello World !"
print("length ==", len(a)) #len ley character kati ota xa dekhaunxa yesley space laii aani " yesto laii ni count garxa 



txt = "The best things in life are free!"
print("free" in txt)    #in ley tyo free vanni text mathi ko paragraph ma xa ki naii check garxa xa vani true xaina vani false 



txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


b = "Hello, World!"
print(b[0:5])
print(b[:5])
print(b[2:])
print(b[-2:-5])  #- ley paxadi bata count garxa
print(b[:-5])
print(b[-2:])
print(b.upper())  #sabaii capital ma lagxa
print(b.lower())   #sabaii small ma lagna yo cahi gaming ma use hunxa
print(b.capitalize())   #aagadi ko aauta word matra capital banaunxa


b= "Hello                     "
print(b.strip())  #strip ley nacahini white space haru hataiidinxa


b="Hello, World!"
print(b.replace("World", "Roshna")) #replace garidinxa
z=b.split(",")  #form banauda use hunxa 
print(z)



#print garni 3 ota tarika

print("Hello World")

name = input ("Enter your name :")

print("You have entered your name = " + name)               #String concant
print(f"You have entered your name =  { name } ")          #string format
print("You have entered your name = %s" % (name))           #modules operator 

"""


empty_list = []                #empty list 
empty_list.append("apple")   
empty_list.append("banana")   # append ley tyo empty_list vanni thau ma add garidinxa 
print(empty_list)             # print the list 


empty_list.remove("banana")  #remove item
print(empty_list)

empty_list.append("apple")   
empty_list.append("banana")
empty_list.append("apple")   
empty_list.append("banana")
for fruit in empty_list :
    print(fruit)

for index, fruit in enumerate(empty_list):       #yesley position pani dinxa
    print(f"Item position : {index} and value: {fruit} ")



#tuple

fruits = ("apple", "banana", "cherry", "kiwi", "strawberry")
print(fruits[1])                        #print second item
(green, yellow , *red) = fruits         # * yo sign ley cahi sabaii kura aauta list banayara aautaii ma rakhidinxa

print(green, yellow, red)
(green, *yellow, red) = fruits
print(green, yellow, red)


#Set

fruits = {"apple", "banana", "cherry", "kiwi", "strawberry"}

for item in fruits:
    print(item)

fruits.add("mango")
print(fruits)


#Dictionaries

