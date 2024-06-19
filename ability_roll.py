import random # Gives access to the .randint() method

def ability_roll():
    # Generates 4 random numbers between 1 and 6 (4d6)
    die_a = random.randint(1, 6)
    die_b = random.randint(1, 6)
    die_c = random.randint(1, 6)
    die_d = random.randint(1, 6)

    # Adds all four dice together
    pre_ability = die_a + die_b + die_c + die_d

    # Subtracts the smallest of the dice (4d6, drop lowest)
    ability = pre_ability - min(die_a, die_b, die_c, die_d)

    # This is the "output" of the function!
    return ability