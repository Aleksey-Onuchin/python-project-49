from random import randint
from random import choice

GAME_RULE = 'What is the result of the expression?'


def get_game():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    operator = choice(['+', '-', '*'])
    question = f'{num1} {operator} {num2}'
    correct_answer = calculate_expression(num1, num2, operator)
    return question, correct_answer


def calculate_expression(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2
