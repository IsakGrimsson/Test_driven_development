import os

def return_recipes():
    list_to_return = []
    # Create a filepath to the data folder
    folder_path = os.getcwd()+"\\\\"+"..\\\\data"
    files = os.listdir(folder_path)
    for file_name in files:
        list_to_return.append(file_name)
    return list_to_return

def select_recipes():
    selected_recipes = []
    recipe_list = enumerate(return_recipes(), 1)
    escape_chars = ["X","x",
                    "Exit","exit","EXIT"]
    yes = ["YES", "Yes", "yes", "y", "Y",
           "True", "true", "TRUE"]
    for i, recipe in recipe_list:
        print(f"{i}. {recipe}")
    while(True):
        while(True):
            user_input = input("Please select a recipe by number, or enter X to end")
            if user_input in escape_chars:
                break
            selected_recipes.append(input("Please select a recipe by number:"))
        user_input = input("Are these all the items you wish to add? enter Y to confirm, otherwise enter any key to add more items")
        if user_input in yes:
            break
    return select_recipes()