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
import time
import random 
import os
import sys

PET_FILE = "PET.txt"




class MyPet:
     def __init__(self, name):
    
      self.pet_name = name
      self.hunger = 50
      self.happiness = 50
      self.energy = 50


     def feed_pet(self):
        self.hunger = min(100, self.hunger + 20)
        if self.hunger <= 0:
            print("Game Over!!")
            sys.exit(0)
        print(f"\n{self.pet_name} hunger level increased to {self.hunger}")
        
        
     def play_pet(self):
            self.happiness = min(100, self.happiness + 20)
            self.energy = max (0, self.energy-10)
            if( self.happiness <=0 or self.energy<=0):
                print("Game Over!!")
                sys.exit(0)
            print(f"\n{self.pet_name} happiness increased to {self.happiness} and engery decreased to {self.energy}")
     
     def rest_pet(self):
           self.energy = min(100, self.energy + 20)
           self.hunger = max(0, self.hunger-5)
           if (self.hunger <=0 or self.energy <= 0):
                print('Game Over!!!')
                sys.exit(0)
           print(f"\n{self.pet_name} energy increased to {self.energy} and hunger decreased to {self.hunger}") 

     

       
def pet_game (pet):
          while True:
              print("\n== Update the pet ==")
              print("1.Feed the pet")
              print("2.Play with pet")
              print("3.Rest Time")
              print("4.save and Exit to main menu")
              choice = input("Enter your choice(1/2/3/4): " ).strip()
           
              if choice == "1":
                  pet.feed_pet()
              elif choice == "2":
                  pet.play_pet()
              elif choice == "3":
                  pet.rest_pet()
              elif choice =="4":
                  print(f"\nReturning to the main menu, {pet.pet_name}!")
                  break
              else:
                  print("Invalid choice.Please try again. ")  
             
def main ():
        pet=None
        while True :
             print("\nWhat would you like to do?")
             print("1.Update the pet")
             print("2.View the status")
             print("3.Quit and save progress") 

             choice = input("Enter your choice(1/2/3): " ).strip()
             if choice == "1":
               if not pet:
                    pet_name=input("Enter your pet name:".strip())
                    pet=MyPet(pet_name)
                   
               pet_game(pet)
                        
             elif choice == "2":
               if pet:
                    pet.status_pet()
               else:
                    print("\n You don't have a pet yet. Please create one first.")
             elif choice =="3":
               print("Goodbye!")
               break
             else:
               print("Invalid choice.Please try again. ") 


              
        
if __name__ == "__main__":
     main()




    




