batteries = [50, 30, 4, 45, 12, 18, 30]   #battery basket

minimun_battery_power = 20             # battery use minimum 20% 

usable_battery_power = 0              # battery 0 power 0 
usable_battery_count = 0              #usable battery 0
for battery in batteries:              # check every battery
    if battery > minimun_battery_power:       #check if battery is over charge 20% to use
        usable_battery_power += battery
        usable_battery_count += 1 
print(f"There are {usable_battery_count} batteries which can be used to generate { usable_battery_power} power")





print("............................Alien Message Decoder...................................")


alien_message = "Hi Human how are you, I am an alien"
print(alien_message[::-1])


alien_message= "neila na ma I ,uoy era woh namuH iH"

print(f"""
      Alien message = {alien_message}
      
      Now, Human meaage = {alien_message[::-1]}   #reverse string
      """)



print("..................................Resource Allocation......................................")

available_foods = [
    "apple",
    "banana",
    "watermelon",
    "Chocolate",
    "Kiwi",
    "Avocado",
    "Grapes",
    "Cherry",
    "berries",
    "cupcakes",
    "pizza",
    "burger",
    "Sweets",
]
available_crews = 3 
each_crew_food = len(available_foods) // available_crews
remaining_food_count = len(available_foods) % available_crews
print(f"Each crew get {each_crew_food} food and Remaining food count = {remaining_food_count}") 

###########################################################################################################################################################
print("..............................................fun game.......................................................")

def setup_mission():
    print("Setting up for the mission........")
    available_foods = [
    "apple",
    "banana",
    "watermelon",
    "Chocolate",
    "Kiwi",
    "Avocado",
    "Grapes",
    "Cherry",
    "berries",
    "cupcakes",
    "pizza",
    "burger",
    "Sweets",
]
    available_crews = int(input("Enter available crews : "))
    print("Setup Completed")
    return available_crews, available_foods

def alien_attack_game(): 
    print("Welcome to Alien Attack Game")
    print("Starting mission.................")

    crews_number, foods = setup_mission ()
    print(f"You have {crews_number} astronuts and food available = {foods}")

    print("WELCOME TO THE MARS!!!!!!!!")

    print("Your Battery is dead please charge the battery")

    print("Mission completed")

alien_attack_game()

