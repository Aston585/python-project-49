import prompt
from random import randint


def even_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'")
    count_right_answer = 0
    while count_right_answer < 3:
        # The range of random numbers will be from 0 to 100
        number = randint(0, 100)
        print(f"Questions: {number}")
        answer_user = prompt.string('Your answer: ')
        if answer_user == str('yes') or str('no'):
            if number % 2 == 0 and answer_user == str('yes'):
                print('Correct!')
                count_right_answer += 1
            elif number % 2 != 0 and answer_user == str('no'):
                print('Correct!')
                count_right_answer += 1
            else:
                print(f"""'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
                break
        elif print("Answer 'yes' if the number is even, otherwise answer 'no'"):
            break
    if count_right_answer == 3:
        print(f"Congratulations, {name}!")
