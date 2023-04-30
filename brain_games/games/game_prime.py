from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    num_to_check = 2
    divisors_quantity = 0
    while num_to_check < num:
        if num % num_to_check == 0:
            divisors_quantity += 1
        num_to_check += 1
    return divisors_quantity == 0


def get_game():
    num = randint(2, 100)
    question = num
    correct_answer = 'yes' if is_prime(num) is True else 'no'
    return question, correct_answer
