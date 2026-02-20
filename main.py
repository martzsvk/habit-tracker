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

# Function for creating json file
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

# Open json file if user has already added habits
try:
    habits_list = open_json()
    # Printing user's habits
    print(f"These are your's habits:\n{habits_list}")

# If not, create it
except FileNotFoundError:
    # List for habits
    habits_list = []
    # Create json file
    create_json()


# Adding habit
add_habit()
