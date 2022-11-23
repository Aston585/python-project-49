import random

RULES = "What number is missing in the progression?"


def game():
    # Formation of a random progression:
    len_progression = random.randint(5, 10)
    step = random.randint(1, 10)
    number = random.randint(1, 100)
    progression = [number]
    while len(progression) != len_progression:
        number += step
        progression.append(number)
    # Selecting the missing element of the progression:
    missing_index = random.randint(0, len(progression) - 1)
    missing_number = progression[missing_index]
    # Progression for player with missing element:
    progression[missing_index] = '..'
    progression_in_string = [str(i) for i in progression]
    progression_for_user = ' '.join(progression_in_string)
    return (progression_for_user, str(missing_number))
