import csv
import shutil
import os

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


def user_input_recipe():
    file_name = input("Please enter the name of the recipe you would like to add: ")
    ingredients = []
    while (True):
        ingredient = []
        ingredient.append(input("Please enter the ingredient you would like to add: "))
        ingredient.append(input("Please enter the unit measurement: "))
        ingredient.append(input("Please enter the quantity: "))
        ingredient.append(input("Is this a staple ingredient? "))
        ingredients.append(ingredient)

        if user_wants_to_continue("Do you wish to add another ingredient?") == False:
            break

    return file_name,ingredients

def create_csv_file():
    # Collect user input
    file_name, ingredients = user_input_recipe()

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Unit", "Number", "Staple"])  # Write the header row
        writer.writerows(ingredients)  # Write the data rows

    # Move the file to a data folder
    current_path = os.getcwd() + "\\" + file_name
    shutil.move(current_path, "../data")




