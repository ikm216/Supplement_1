def add(num1, num2):
    """ Adds two numbers and returns the result

    Args:
        num1: the first summand
        num2: the second summand

    Returns:
        The sum of the two numbers
    """
    return num1 + num2

def count(string):
     """ Count the length of the string

    Args:
        string: the string being counted

    Returns:
        The number of characters in the string
    """
     return len(string)

def upsert(dictionary, key, value):
    """ Upserts a value into the dictionary

    The value must implement addition with itself

    Args:
        dictionary: the dictionary to upsert
        key: the key of the dictionary for the upsert
        value: the value being upserted

    Returns:
        The updated dictionary with the upserted value
    """
    if key in dictionary.keys():
        #dictionary contains key, update
        dictionary[key] = dictionary[key] + value
    else:
        #dictionary does not contain key, set
        dictionary[key] = value

def test_should_return_four_for_two_and_two():
    assert add(2, 2) == 4

def test_should_return_length_five_for_hello():
    assert count("hello") == 5

def test_should_insert_new_key():
    dictionary = {}
    key = "test"
    upsert(dictionary, key, 5)
    assert dictionary[key] == 5

def test_should_append_new_key():
    dictionary = {}
    key = "test"
    upsert(dictionary, key, 5)
    upsert(dictionary, key, 2)
    assert dictionary[key] == 7
