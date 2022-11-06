import prompt
from random import randint


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")


def rules_of_the_game():
    print(f"Answer 'yes' if the number is even, otherwise answer 'no'")


def even_game():
    count_right_answer = 0
    while count_right_answer < 3:
        number = randint(0, 100) #The range of random numbers will be from 0 to 100
        print(f"Questions: {number}")
        answer_user = prompt.string('Your answer: ')
        if answer_user == str('yes') or str('no'):
            if number % 2 == 0 and answer_user == str('yes'):
                print('Correct!')
                count_right_answer += 1
            else:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {welcome_user.name}!")
                break
        else:
            print("Answer 'yes' if the number is even, otherwise answer 'no'")
            break
    if count_right_answer == 3:
        print(f"Congratulations, {welcome_user.name}!")
