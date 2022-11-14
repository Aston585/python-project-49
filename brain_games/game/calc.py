import prompt
import random


def calc_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    count_right_answer = 0
    while count_right_answer < 3:
        # The range of random numbers will be from 0 to 10
        number_first = random.randint(0, 10)
        number_second = random.randint(0, 10)
        operator = ('+', '-', '*')
        expression = f"{number_first} {random.choice(operator)} {number_second}"
        print("What is the result of the expression?")
        print(f"Question: {expression}")
        answer_user = prompt.string('Your answer: ')
        if operator == '+':
            result = number_first + number_second
        elif operator == '-':
            result = number_first - number_second
        elif operator == '*':
            result = number_first * number_second
        if answer_user == result:
            print('Correct!')
            count_right_answer += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer" 
                  f"was '{result}'\nLet's try again, {name}!")
            break
        if count_right_answer == 3:
            print(f"Congratulations, {name}!")
            break
