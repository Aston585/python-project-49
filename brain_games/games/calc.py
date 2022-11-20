import random

rules = "What is the result of the expression?"
number_first = random.randint(0, 10)
number_second = random.randint(0, 10)
operators = ('+', '-', '*')
random_operator = random.choice(operators)
expression = f"{number_first} {random_operator} {number_second}"
question = f"Question: {expression}"


def calc(random_operator):
    result = 0
    if random_operator in '+':
        result = number_first + number_second
    elif random_operator in '-':
        result = number_first - number_second
    elif random_operator in '*':
        result = number_first * number_second
    return str(result)


correct_answer = calc(random_operator)
