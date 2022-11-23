import random

RULES = "What is the result of the expression?"


def game():
    first_operand = random.randint(0, 10)
    second_operand = random.randint(0, 10)
    operators = ('+', '-', '*')
    random_operator = random.choice(operators)
    expression = f"{first_operand} {random_operator} {second_operand}"
    result = 0
    if random_operator == '+':
        result = first_operand + second_operand
    elif random_operator == '-':
        result = first_operand - second_operand
    elif random_operator == '*':
        result = first_operand * second_operand
    return (expression, str(result))
