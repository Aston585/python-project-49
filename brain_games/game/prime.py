import prompt
from random import randint
import math


def prime_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count_right_answer = 0
    while count_right_answer < 3:
        number = randint(2, 100)
        # The range of random numbers will be from 0 to 100
        print(f"Question: {number}")
        answer_user = prompt.string('Your answer: ')
        if answer_user in ('yes', 'no'):
            def is_prime(number):
                for i in range(2, int(math.sqrt(number)) + 1):
                    if number % i == 0:
                        return False
                return True
            if is_prime(number) and answer_user == str('yes'):
                print('Correct!')
                count_right_answer += 1
            elif not is_prime(number) and answer_user == str('no'):
                print('Correct!')
                count_right_answer += 1
            else:
                print(f"'{answer_user}' is wrong answer ;(\nLet's try " 
                      f"again, {name}!")
                break
        else:
            print("Answer 'yes' if the number is prime, otherwise answer 'no'")
            break
    if count_right_answer == 3:
        print(f"Congratulations, {name}!")
