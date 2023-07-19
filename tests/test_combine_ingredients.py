from modules.combine_ingredients import *

def test_combine_ingredients():
    # Mock recipes returned by the select_recipes function
    selected_recipes = ["Pancakes", "Fish curry"]
    # Mock ingredients
    ingredients = sorted((["Red Pepper", "X", "2"], ["Lime", "X", "1"], ["Egg", "X", "3"]))

    assert sorted(combine_ingredients(selected_recipes)) == ingredients