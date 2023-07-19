import re

def format_name(string):
    cleaned_string = string.replace("-", " ").replace("_", " ")
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', cleaned_string)
    formatted_string = cleaned_string.strip().lower().capitalize()
    return formatted_string

def format_unit(string):
    cleaned_string = string.replace("-", " ").replace("_", " ")
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', cleaned_string)
    formatted_string = cleaned_string.strip().lower()

    accepted_units = ["x","l","ml","grams","kg","cup","tsp","tbsp","can",
                      "pinch","clove","bulb"]
    if formatted_string in accepted_units:
        return formatted_string
    return False

def format_number(string):
    if string.isdigit():
        return string
    return False

def format_staple(string):
    cleaned_string = string.replace("-", " ").replace("_", " ")
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', cleaned_string)
    formatted_string = cleaned_string.strip().lower().capitalize()
    if formatted_string == "False" or formatted_string == "True":
        return formatted_string
    return False

