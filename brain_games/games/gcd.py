import random
import math

rules = "Find the greatest common divisor of given numbers."
number_first = random.randint(1, 100)
number_second = random.randint(1, 100)
example = f"{number_first} {number_second}"
question = f"Question: {example}"


def gcd(number_first, number_second):
    result = math.gcd(number_first, number_second)
    return str(result)


correct_answer = gcd(number_first, number_second)
