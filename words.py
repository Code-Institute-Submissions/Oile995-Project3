import random


animals = [
    "alligator",
    "badger",
    "cheetah",
    "dolphin",
    "elephant",
    ]


def get_word(category):
    """
    This function gets called with the theme choice parameter
    and gets a random word from choosen word list.
    """
    if(category == 1):
        random_word = random.choice(animals)
    else:
        print("did not choose animals")
    
    return random_word.upper()