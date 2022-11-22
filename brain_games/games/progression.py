import random


rules = "What number is missing in the progression?"


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
    lost_index = random.randint(0, len(progression) - 1)
    lost_number = progression[lost_index]
    # Progression for player with missing element:
    progression.pop(lost_index)
    progression.insert(lost_index, '..')
    progression_in_string = [str(i) for i in progression]
    progression_for_user = ' '.join(progression_in_string)
    question_answer = (progression_for_user, str(lost_number))
    return question_answer
