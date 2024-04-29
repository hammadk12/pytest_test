from my_test import age
from my_test import main

def testing_age():
    assert age("12") == "age: 12"

def testing_default():
    assert age() == "age: 18"

def testing_main():
    assert main("21") == "You are good to go, 21"