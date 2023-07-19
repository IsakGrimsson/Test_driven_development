import csv
import shutil
import os

from modules.format_user_input import *

def user_wants_to_continue(prompt_for_user):
    continue_yes_or_no = ""
    yes = ["YES", "Yes", "yes", "y", "Y",
           "True", "true", "TRUE"]
    no = ["NO", "No", "no", "n", "N",
          "False", "false", "FALSE"]
    continue_yes_or_no = input(prompt_for_user)
    while not (continue_yes_or_no in yes or continue_yes_or_no in no):
        continue_yes_or_no = input(
            "I'm sorry I didn't undestand that command. Please answer either yes or no [y/n]")
    if continue_yes_or_no in no:
        return False
    if continue_yes_or_no in yes:
        return True

def get_user_input(type):
    if type == "name":
        return format_name(input("Please enter the ingredient you would like to add: "))
    elif type == "unit":
        string = format_unit(input("Please enter the unit measurement: "))
        while(True):
            if string == False:
                string = format_unit(input("We can't accept that measurement unit, try again: "))
            else:
                break
    elif type == "number":
        string = format_number(input("Please enter the quantity: "))
        while (True):
            if string == False:
                string = format_unit(input("We can't accept that number, try again: "))
            else:
                break
    elif type == "staple":
        string = format_staple(input("Is this a staple ingredient? "))
        while (True):
            if string == False:
                string = format_unit(input("That isn't True or False, try again: "))
            else:
                break
    elif type == "title":
        string = format_name(input("Please enter the name of the recipe you would like to add: "))
    else:
        print("Unexpected error in get_user_input()")
    return string



def get_user_input_recipe():
    file_name = get_user_input("title")
    print(file_name)
    ingredients = []
    while (True):
        ingredient = []
        ingredient.append(get_user_input("name"))
        ingredient.append(get_user_input("unit"))
        ingredient.append(get_user_input("number"))
        ingredient.append(get_user_input("staple"))
        ingredients.append(ingredient)

        if user_wants_to_continue("Do you wish to add another ingredient?") == False:
            break

    return file_name, ingredients

def create_csv_file():
    # Collect user input
    file_name, ingredients = get_user_input_recipe()

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Unit", "Number", "Staple"])  # Write the header row
        writer.writerows(ingredients)  # Write the data rows

    # Move the file to a data folder
    current_path = os.getcwd() + "\\" + file_name
    shutil.move(current_path, "../data")




