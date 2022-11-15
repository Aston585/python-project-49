import prompt
import random


def progression_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    count_right_answer = 0
    while count_right_answer < 3:
        print("What number is missing in the progression?")
        step = random.randint(1, 10)
        number = random.randint(1, 100)
        len_progression = random.randint(5, 10)
        progression = [number]
        while len(progression) != len_progression:
            number += step
            progression.append(number)
        lost_index = random.randint(0, len(progression) - 1)
        lost_number = progression[lost_index]
        progression.pop(lost_index)
        progression.insert(lost_index, '..')
        progression_in_string = [str(i) for i in progression]
        progression_for_user = ' '.join(progression_in_string)
        print(f"Question: {progression_for_user}")
        answer_user = prompt.string('Your answer: ')
        if answer_user == str(lost_number):
            print('Correct!')
            count_right_answer += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer" 
                  f"was '{lost_number}'\nLet's try again, {name}!")
            break
        if count_right_answer == 3:
            print(f"Congratulations, {name}!")
            break
