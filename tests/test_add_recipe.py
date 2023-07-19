import os

from modules.add_recipe import *

# Mock user inputs for testing
user_inputs = [
    "Protein_tuna_salad",
    "tuna", "can", "1", False, "Yes",
    "cottage cheese", "gram", "300", False,"N"
]

def test_create_csv(monkeypatch):
    # Simulate the inputs above
    inputs = iter(user_inputs)
    def mock_input(prompt):
        value = next(inputs)
        return value
    monkeypatch.setattr("builtins.input", mock_input)

    # Run the function with the mock user input
    create_csv_file()

    # Check if the CSV file is created
    main_directory = os.path.dirname(os.getcwd())
    data_folder = os.path.join(main_directory, "data")
    csv_file_path = os.path.join(data_folder, "Protein_tuna_salad")
    assert os.path.isfile(csv_file_path)

    # Read the contents of the CSV file
    with open(csv_file_path, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Check the header row
    assert rows[0] == ["Name", "Unit", "Number", "Staple"]
    # Check the data rows
    assert rows[1] == ["tuna", "can", '1', 'False']
    assert rows[2] == ["cottage cheese", "gram", '300', 'False']
    # Clean up: remove the test CSV file
    os.remove(csv_file_path)