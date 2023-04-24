from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game():
    num = randint(2, 100)
    question = num
    correct_answer = 'yes' if is_prime(num) is True else 'no'
    return question, correct_answer


def is_prime(num):
    i = 2
    k = 0
    while i < num:
        if num % i == 0:
            k += 1
        i += 1
    return k == 0
