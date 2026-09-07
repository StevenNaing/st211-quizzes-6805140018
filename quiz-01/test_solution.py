from solution import add_numbers

def test_add_numbers_basic():
    assert add_numbers(2, 3) == 5

def test_add_numbers_negative():
    assert add_numbers(-1, 1) == 0