from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_game():
    num = randint(1, 20)
    question = num
    correct_answer = 'yes' if is_even(num) is True else 'no'
    return question, correct_answer
