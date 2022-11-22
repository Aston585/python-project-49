from random import randint
import math

rules = """Answer "yes" if given number is prime. Otherwise answer "no"."""


def game():
    number = randint(2, 100)
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            result = str('no')
            break
    else:
        result = str('yes')
    question_answer = (number, result)
    return question_answer
