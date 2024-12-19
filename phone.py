"""

def my_phonebook ():
    a = input("Enter your name : ")
    if a == thisdict["Name"]:
        print(thisdict)
    else:
        print("User not found")
thisdict = {
    "Name" : "Roshna",
    "Phone_Number" : 9803589813
}
thisdict = {
    "Name" : "Salina",
    "Phone_Number" : 9800000123
}
thisdict = {
    "Name" : "Prakriti",
    "Phone_Number" : 98000003567
}
thisdict = {
    "Name" : "Unisha",
    "Phone_Number" : 980356789
}
thisdict = {
    "Name" : "Reshna",
    "Phone_Number" : 9712345678
}
thisdict = {
    "Name" : "Dipika",
    "Phone_Number" : 986786868
}

my_phonebook()
"""


#Simple Phone book
"""
-Add user with Phone number
-Save
-get number with name
-loop add many users

solution
-get number and name
-once data get -> store data -> dict {"name":number}
-repeat untile user exit
"""


def store_contact(name, number, contacts={}):
    contacts[name.lower()] = number 
    return contacts

def phone_book():
    contacts ={}
    while True:
        name = input("Enter name : ")
        number = input ("Enter number : ")
        contacts = store_contact(name, number, contacts)
        user_choice = input("""
Do you want to exit?
                            1. Yes
                            2. NO
""")
        if user_choice == "1":
          return contacts

my_contact_book = phone_book()

def get_phone_number(name, contacts):
    return contacts.get(name.lower())

user_name = input("Enter name to find phone number : ")
print(get_phone_number(user_name, my_contact_book))