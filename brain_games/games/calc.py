import random

rules = "What is the result of the expression?"


def game():
    number_first = random.randint(0, 10)
    number_second = random.randint(0, 10)
    operators = ('+', '-', '*')
    random_operator = random.choice(operators)
    expression = f"{number_first} {random_operator} {number_second}"
    result = 0
    if random_operator in '+':
        result = number_first + number_second
    elif random_operator in '-':
        result = number_first - number_second
    elif random_operator in '*':
        result = number_first * number_second
    question_answer = (expression, str(result))
    return question_answer
