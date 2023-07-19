from modules.select_recipes import *
from collections import Counter

def test_return_recipes():
    # Recipes used for testing
    recipes_that_should_be_returned = sorted(["Protein tuna salad", "Pancakes", "Fish curry"])
    returned_recipes = sorted(return_recipes())
    assert returned_recipes == recipes_that_should_be_returned

def test_select_recipes(monkeypatch):
    # Mock user inputs for testing
    user_inputs = [
        "1", "X", "False", "2", "X", "Yes"
    ]
    # Simulate the inputs above
    inputs = iter(user_inputs)
    def mock_input(prompt):
        value = next(inputs)
        return value
    monkeypatch.setattr("builtins.input", mock_input)

    list_of_recipes = sorted(select_recipes())
    assert list_of_recipes == sorted(["Pancakes", "Fish curry"])
