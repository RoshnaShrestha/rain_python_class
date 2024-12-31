"""
#OOP:

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)



#####..............................................................

class Person:
    def __init__(self, name,age):    #dunder method or magic : self call, __init__ : runs when object create
        self.name = name
        self.age = age

roshna = Person("Roshna", "19")

print(roshna.name)
print(roshna.age)


class PhoneFactory:
    model: None
    color: None
    is_android: None

    def __init__(self, model, color, is_android):   
        self.model = model
        self.color = color
        self.is_android = is_android
        print("Phone created")

    def __str__ (self):
        return f"{self.model} - {self.color}"
        
    def check_os(self):
        if self.is_android:
            print("Android")

        else:
            print("ios")

oppo_phone_1 = PhoneFactory("A53", "Black", True)
print (oppo_phone_1)



"""






#To do list using python class and object


import os


TODOLIST_FILE = "todolist.txt"

def save_to_file(filename, data, mode = "a"):
    """Save data to file"""
    with open(filename, mode) as file:
        file.write(data +"\n")

def load_from_file(filename):
    """Load data from a file """
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file]

class TodoList:
    def __init__(self):
        self.tasks = load_from_file(TODOLIST_FILE)

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the list.")
        else:
            print(f"Task '{task}' not found in the list.")

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print(f"Taks update to '{new_task}'.")

        else:
            print(f"Task '{old_task}' not found in the list.")    

    def show_tasks(self):
        if self.tasks:
            print("Your Todo List:")
            for index, task in enumerate(self.tasks):
                print(f"{index+1}.{task}")

        else:
            print("Your Todo List is empty.")

todo_list = TodoList()


todo_list.add_task("Buy groceries")
todo_list.add_task("Do homework")
todo_list.add_task("Call Mom")

todo_list.show_tasks()
todo_list.remove_task("Finish the report")
todo_list.update_task("Buy groceries", "Go for a walk")
todo_list.show_tasks()










import os

BACKUP_FILE = "backup.txt"

def save_to_file(filename, data, mode="a"):
    """Save data to file."""
    with open(filename, mode) as file:
        file.write(data + "\n")

def load_from_file(filename):
    """Load data from a file."""

class ToDoList:
    def __init__(self):
        self.tasks = load_from_file(BACKUP_FILE)

    def add_task(self, task):
        self.tasks.append(task)
        save_to_file(BACKUP_FILE, task)
        print(f"Task '{task}' added to the list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' has been removed.")
            self._backup_tasks()
        else:
            print(f"No such task '{task}' exists.")

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print(f"Task updated from '{old_task}' to '{new_task}'.")
            self._backup_tasks()
        else:
            print(f"'{old_task}' is not present in the list.")

    def show_tasks(self):
        if self.tasks:
            print("Your Todo List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Your Todo List is empty.")

    def _backup_tasks(self):
        """Rewrites all tasks to the backup file."""
        with open(BACKUP_FILE, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")


# Main execution
todo_list = ToDoList()

todo_list.add_task("Buy groceries")
todo_list.add_task("Do homework")
todo_list.add_task("Call Mom")

todo_list.show_tasks()

todo_list.remove_task("Finish the report")
todo_list.update_task("Buy groceries", "Go for a walk")
todo_list.show_tasks()