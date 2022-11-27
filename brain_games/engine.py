import prompt

ROUNDS_COUNT = 3


def play(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.RULES)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.create_game_data()
        print(f"Question: {question}")
        answer_user = prompt.string('Your answer: ')
        if answer_user.lower() in correct_answer:
            print('Correct!')
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer"
                  f" was '{correct_answer}'\nLet's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
