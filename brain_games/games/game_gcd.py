from random import randint

task = 'Find the greatest common divisor of given numbers.'


def gcd():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    question = f'{num1} {num2}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    correct_answer = (num1 + num2)
    return (question, correct_answer)
