from modules.format_user_input import *

def test_format_name():
    test_strings = ["hello_world! how-are_you?", "tHIS-iS_A_tEST!", "---a-b-c-d-e---", "123!@#_test_456"]
    expected_strings = ["Hello world how are you", "This is a test", "A b c d e", "Test"]
    for test_string, expected_string in zip(test_strings, expected_strings):
        assert format_name(test_string) == expected_string

def test_format_unit():
    test_strings = ["This test should fail", "this too", "mhmmm","another_one"," ","True",
                    "x","l","ml","grams","kg","cup","tsp","tbsp","can","pinch","clove","bulb",
                   "X","L","Ml","Grams","Kg","Cup","Tsp","Tbsp","Can","Pinch","Clove","Bulb"]
    expected_strings = [False, False, False, False, False, False,
                        "x","l","ml","grams","kg","cup","tsp","tbsp","can","pinch","clove","bulb",
                        "x","l","ml","grams","kg","cup","tsp","tbsp","can","pinch","clove","bulb"]
    for test_string, expected_string in zip(test_strings, expected_strings):
        assert format_unit(test_string) == expected_string

def test_format_number():
    test_strings = ["123","456","789","987","654","321",
                   "hello","world","test","example","random","string"]
    expected_strings = [True, True, True, True, True, True,
                        False,False,False,False,False,False]
    for test_string, expected_string in zip(test_strings, expected_strings):
        assert format_number(test_string) == expected_string

def test_format_staple():
    test_strings = ["$True", "true", "TRUE", "False", "false_", "FALSE!",
                   "1", "0", "Truer", "falsey", "T", "f"]
    expected_strings = [True, True, True, True, True, True,
                        False, False, False, False, False, False]
    for test_string, expected_string in zip(test_strings, expected_strings):
        assert format_staple(test_string) == expected_string



