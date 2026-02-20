from datetime import datetime as dt
import json


# Today's date
time_now = dt.now()
today_date = time_now.strftime("%d.%m.%Y")


# Function to ask user to add habit
def add_habit():
    new_habit = input("Please add some habit (e.g. programming, gym): ")
    # Adding habit to habits list
    habits_list.append({"date": today_date, "habit": new_habit, "completed": False})
    # Update json through create_json function
    create_json()

# Function for creating and updating json file
def create_json():
    # Creating json file
    with open("habits.json", "w") as file:
        json.dump(habits_list, file)

# Function for opening json
def open_json():
    with open("habits.json") as data:
        return json.load(data)


# Introduction
print("Welcome to my Habit Tracker")

try:
    # Load existing habits from json file
    habits_list = open_json()
except FileNotFoundError:
    # If there is non, start with an empty list 
    habits_list = []

# While loop to add more habits or show habits
adding = True
while adding:
    # Print options
    print("Type 1 to add habit - 2 to show habits - 3 to exit")
    what_to_do = input("Enter a number please: ")

    if what_to_do == "1":
        add_habit()
        print("Habit added successfully!")

    elif what_to_do == "2":
        try:
            # Printing user's habits
            print(f"These are your's habits:\n{habits_list}")
        except FileNotFoundError:
            print("Sorry you don't have any saved habits yet.")

    elif what_to_do == "3":
        adding = False

    else:
        print("You entered wrong number or format. Please try again.")
