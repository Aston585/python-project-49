from random import randint
import math

RULES = """Answer "yes" if given number is prime. Otherwise answer "no"."""


def is_prime(number):
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    else:
        return True


def create_game_data():
    number = randint(2, 100)
    if not is_prime(number):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return (number, correct_answer)
