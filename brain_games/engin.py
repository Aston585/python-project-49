import prompt


def game_engin(rules, question, correct_answer):
    print("Welcome to the Brain Games!")  # Приветствие
    name = prompt.string('May I have your name? ')  # Знакомство с игроком
    print(f"Hello, {name}!")
    count_right_answer = 0
    print(rules)  # Объяснение правил
    while count_right_answer < 3:
        print(f"Question: {question}")  # Вопрос игроку
# Вычисление правильного ответа в логике модуля игры
        answer_user = prompt.string('Your answer: ')  # Прием ответа игрока
        if answer_user.lower() == correct_answer:  # Проверка ответа игрока
            print('Correct!')
            count_right_answer += 1
        else:  # Либо окончание игры, либо переход на следующий раунд
            print(f"'{answer_user}' is wrong answer ;(. Correct answer"
                  f" was '{correct_answer}'\nLet's try again, {name}!")
            break
    if count_right_answer == 3:  # Победа
        print(f"Congratulations, {name}!")
