import random


animals = [
    "alligator",
    "badger",
    "cheetah",
    "dolphin",
    "elephant",
    "firefly",
    "golden retriever",
    "mockingbird",
    "starfish",
    "wolverine"
    ]

countries = [
    "Angola",
    "Belgium",
    "Ecuador",
    "Canada",
    "Kazakhstan",
    "Mozambique",
    "Thailand",
    "Sweden",
    "United Kingdom"
    ]

food = [
    "baked beans",
    "Tacos",
    "Hamburger",
    "Pizza",
    "Lasagna",
    "Sallad",
    "Waffles",
    "Fried chicken",
    "Mashed potatoes",
    "Oatmeal"
    ]


def get_word(category):
    """
    This function gets called with the theme choice parameter
    and gets a random word from choosen word list.
    """
    try:
        if (category == "1"):
            random_word = random.choice(animals)
        elif (category == "2"):
            random_word = random.choice(countries)
        elif (category == "3"):
            random_word = random.choice(food)
    except ValueError:
        print("Error, something went wrong selecting category")
        random_word = random.choice(animals)
        print("Therefore a Animal category was chosen")
    return random_word.upper()
