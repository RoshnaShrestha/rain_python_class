"""
Lists:
Create a list named my_list containing the following elements: 1, 2, 3, 'a', 'b', 'c'.
Add the element 'd' to the end of the list.
Remove the element 2 from the list.
Print the length of the list.
Print the list.
"""

my_list = [1, 2, 3, 'a', 'b', 'c']
my_list. append('d')
my_list.remove(2)
print(len(my_list))
print(my_list)



"""
Tuples:
Create a tuple named my_tuple with the following elements: 10, 20, 30, 40, 50.
Access and print the second element of the tuple.
Try to change the third element of the tuple to 35 (expect an error since tuples are immutable).
Print the entire tuple.

"""

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1])
thistuple = list(my_tuple)
thistuple[3] = 35
my_tuple = tuple(thistuple)
print(my_tuple)

"""
Sets:
Create a set named my_set containing the elements: 1, 2, 2, 3, 4, 4, 5.
Add the element 6 to the set.
Remove the element 3 from the set.
Print all elements of the set.
Check if the element 4 is in the set and print the result.

"""
my_set = {1, 2, 2, 3, 4, 4, 5}
my_set.add(6)
my_set.remove(3)
print(my_set)
if "4" in my_set:
    print("Yes 4 in my_set") 
else:
    print("4 is not in my_set")