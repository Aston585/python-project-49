import prompt


def game_engin(games):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    count_right_answer = 0
    print(games.RULES)
    while count_right_answer < 3:
        question, correct_answer = games.game()
        print(f"Question: {question}")
        answer_user = prompt.string('Your answer: ')
        if answer_user.lower() in correct_answer:
            print('Correct!')
            count_right_answer += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer"
                  f" was '{correct_answer}'\nLet's try again, {name}!")
            break
    if count_right_answer == 3:
        print(f"Congratulations, {name}!")
