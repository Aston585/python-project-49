from random import randint
import math

RULES = """Answer "yes" if given number is prime. Otherwise answer "no"."""


def is_prime():
    number = randint(2, 100)
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False, number
    else:
        return True, number


def game():
    answer, number = is_prime()
    if not answer:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return (number, correct_answer)
