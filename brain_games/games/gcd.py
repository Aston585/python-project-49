import random
import math

rules = "Find the greatest common divisor of given numbers."


def game():
    number_first = random.randint(1, 100)
    number_second = random.randint(1, 100)
    example = f"{number_first} {number_second}"
    result = math.gcd(number_first, number_second)
    question_answer = (example, str(result))
    return question_answer
