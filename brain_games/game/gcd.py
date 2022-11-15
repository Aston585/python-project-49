import prompt
import random
import math


def gcd_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    count_right_answer = 0
    while count_right_answer < 3:
        number_first = random.randint(1, 100)
        number_second = random.randint(1, 100)
        # The range of random numbers will be from 1 to 100
        example = f"{number_first} {number_second}"
        print("Find the greatest common divisor of given numbers.")
        print(f"Question: {example}")
        answer_user = prompt.string('Your answer: ')
        result = math.gcd(number_first, number_second)
        if answer_user == str(result):
            print('Correct!')
            count_right_answer += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer" 
                  f"was '{result}'\nLet's try again, {name}!")
            break
        if count_right_answer == 3:
            print(f"Congratulations, {name}!")
            break
