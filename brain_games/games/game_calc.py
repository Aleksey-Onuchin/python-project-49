from random import randint

task = 'What is the result of the expression?'


def calc():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    operand_type = randint(1, 3)
    if operand_type == 1:
        question = f'{num1} + {num2}'
        correct_answer = num1 + num2
    elif operand_type == 2:
        question = f'{num1} - {num2}'
        correct_answer = num1 - num2
    else:
        question = f'{num1} * {num2}'
        correct_answer = num1 * num2
    return (question, correct_answer)
