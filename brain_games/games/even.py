from random import randint


rules = str("""Answer "yes" if the number is even, otherwise answer "no".""")
question = number = randint(0, 100)


def is_even(number):
    if number % 2 == 0:
        return str('yes')
    else:
        return str('no')


correct_answer = is_even(number)
