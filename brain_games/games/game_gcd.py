from random import randint
from math import gcd

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    return gcd(num1, num2)


def get_game():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    question = f'{num1} {num2}'
    correct_answer = find_gcd(num1, num2)
    return question, correct_answer
