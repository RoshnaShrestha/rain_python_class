"""
Tasks:
Setup and Initialization:
Create a program that asks the user to name their pet.
Initialize the pet’s attributes:
Hunger: 50
Happiness: 50
Energy: 50
(Values range from 0 to 100)
Pet Actions:
Implement functions for pet actions:
Feed: Increases hunger level.
Play: Increases happiness, decreases energy.
Rest: Increases energy, slightly decreases hunger.
Add interactive options to let the user choose an action.
Status Check:
Display the pet’s current stats after each action.
Game Rules:
If any attribute reaches 0, the pet gets "sick" and the game ends.
If all attributes are above 80 for three consecutive turns, the pet "wins" by becoming super happy and energetic.
Bonus Challenges:
Add a countdown timer for user input.
Include random events (e.g., the pet finds a toy that boosts happiness).
Create a save/load feature to resume the game later.

"""

import random
pet_name = None
hunger = 50
happiness = 50
energy = 50
        
def feed_pet():
        global hunger 
        hunger = min(100, hunger + 20)
        print(f"\n{pet_name} hunger level increased to {hunger}")

def play_pet():
            global happiness,energy 
            happiness = min(100, happiness + 20)
            energy = max (0, energy-10)
            print(f"\n{pet_name} happiness increased to {happiness} and engery decreased to {energy}")
        
def rest_pet():
           global energy, hunger
           energy = min(100, energy + 20)
           hunger = max(0, hunger-5)
           print(f"\n{pet_name} energy increased to {energy} and hunger decreased to {hunger}") 

def status_pet ():
       print(f"\n Name : {pet_name}, hunger : {hunger}, happiness : {happiness}, energy : {energy}")



def pet_game ():
       print("Welcome to Update the pet!")
       petname = input("What is your pet name ? ")

       while True:
        print("\n== Update the pet ==")
        print("1.Feed the pet")
        print("2.Play with pet")
        print("3.Rest Time")
        print("4.Exit to main menu")
        choice = input("Enter your choice(1/2/3/4): " ).strip()
        if choice == "1":
                feed_pet()
        elif choice == "2":
                play_pet()
        elif choice == "3":
                rest_pet()
        elif choice =="4":
                print(f"\nReturning to the main menu, {pet_name}!")
                break
        else:
             print("Invalid choice.Please try again. ")  
            
def main():
    while True :
        print("\nWhat would you like to do?")
        print("1.Update the pet")
        print("2.View the status")
        print("3.Quit and save progress") 

        choice = input("Enter your choice(1/2/3): " ).strip()

        if choice == "1":
            pet_game()            
        elif choice == "2":
            status_pet()
        elif choice =="3":
                print("Goodbye!")
                break
        else:
            print("Invalid choice.Please try again. ")  

if __name__ == "__main__":
    main()
    




