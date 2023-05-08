import random


animals = [
    "alligator",
    "badger",
    "cheetah",
    "dolphin",
    "elephant",
    ]

countries = [
    "Angola",
    "Belgium",
    "Canada",
    "Sweden"
    ]

food = [
    "Tacos",
    "Hamburger",
    "Pizza",
    "Lasagna",
    "Sallad"
    ]


def get_word(category):
    """
    This function gets called with the theme choice parameter
    and gets a random word from choosen word list.
    """
    if (category == 1):
        random_word = random.choice(animals)
    elif (category == 2):
        random_word = random.choice(countries)
    elif (category == 3):
        random_word = random.choice(food)
    else:
        print("did not choose animals")
    return random_word.upper()
    