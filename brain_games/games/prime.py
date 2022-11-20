from random import randint
import math


rules = """Answer "yes" if given number is prime. Otherwise answer "no"."""
number = randint(2, 100)
question = f"Question: {number}"


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return str('no')
        else:
            return str('yes')


correct_answer = is_prime(number)
