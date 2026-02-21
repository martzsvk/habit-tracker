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
    # Update JSON through create_json function
    create_json()

# Function for creating and updating JSON file
def create_json():
    # Creating json file
    with open("habits.json", "w") as file:
        json.dump(habits_list, file)

# Load data from JSON
def open_json():
    with open("habits.json") as data:
        return json.load(data)

# Function to show habits in prettier form than raw JSON
def show_habits():
    if not habits_list:
        print("Sorry you don't have any habits yet.")
    else:
        for index, habit in enumerate(habits_list, start=1):
            # If completed == True
            if habit["completed"]:
                status = "✔"
            else:
                status = " "
            print(f"{index}. [{status}] {habit['habit']} ({habit['date']})")

# Function to mark habit as completed (== True)
def complete_habit():
    show_habits()

    try:
        which_habit = int(input("Please select habit number: "))
        # Marking habit as completed
        habits_list[which_habit - 1]["completed"] = True
        # Adding this data to JSON
        create_json()
        print("Habit marked as completed!")
    except (IndexError, ValueError):
        print("Sorry something went wrong. Please try again.")


# Introduction
print("Welcome to my Habit Tracker")

try:
    # Load existing habits from json file
    habits_list = open_json()
except FileNotFoundError:
    # If there is none, start with an empty list
    habits_list = []

# While loop to add more habits or show habits
adding = True
while adding:
    # Print options
    print("Type 1 to add habit - 2 to show habits - 3 to mark habit as completed - 4 to exit")
    what_to_do = input("Enter a number please: ")

    if what_to_do == "1":
        add_habit()
        print("Habit added successfully!")

    elif what_to_do == "2":
        show_habits()

    elif what_to_do == "3":
        complete_habit()

    elif what_to_do == "4":
        adding = False

    else:
        print("You entered wrong number or format. Please try again.")
