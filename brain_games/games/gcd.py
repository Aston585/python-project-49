import random
import math

RULES = "Find the greatest common divisor of given numbers."


def game():
    number_first = random.randint(1, 100)
    number_second = random.randint(1, 100)
    expression = f"{number_first} {number_second}"
    result = math.gcd(number_first, number_second)
    return (expression, str(result))
