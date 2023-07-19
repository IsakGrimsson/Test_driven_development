import csv
import shutil
import os

def user_input_recipe():
    file_name = input("Please enter the name of the recipe you would like to add: ")
    ingredients = []
    while (True):
        ingredient = []
        name = input("Please enter the ingredient you would like to add: ")
        ingredient.append(name)
        unit = input("Please enter the unit measurement: ")
        ingredient.append(unit)
        quantity = input("Please enter the quantity: ")
        ingredient.append(quantity)
        staple = input("Is this a staple ingredient? ")
        ingredient.append(staple)

        ingredients.append(ingredient)

        continue_yes_or_no = ""
        yes = ["YES", "Yes", "yes", "y", "Y"]
        no = ["NO", "No", "no", "n", "N"]
        continue_yes_or_no = input("Do you wish to add another ingredient?")
        while not (continue_yes_or_no in yes or continue_yes_or_no in no):
            continue_yes_or_no = input("I'm sorry I didn't undestand that command. Do you wish to add another ingredient? [y/n]")
        if continue_yes_or_no in no:
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




