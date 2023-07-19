import os
import csv

selected_recipes = ["Pancakes", "Fish curry"]


def combine_ingredients(selected_recipes):
    list_to_return = []

    # Create a filepath to the data folder
    folder_path = os.getcwd() + "\\\\" + "..\\\\data"

    for recipe_name in selected_recipes:
        file_path = folder_path + "\\\\" + recipe_name

        with open(file_path, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            # Skip the header
            next(csvreader)
            for row in csvreader:
                if row[-1] == "False":
                    list_to_return.append(row[:-1])

    return list_to_return