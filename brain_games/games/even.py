from random import randint


rules = str("""Answer "yes" if the number is even, otherwise answer "no".""")


def game():
    number = randint(0, 100)
    if number % 2 == 0:
        value = str('yes')
    else:
        value = str('no')
    question_answer = (number, value)
    return question_answer
