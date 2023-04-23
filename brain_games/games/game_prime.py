from random import randint

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():
    question = randint(2, 100)
    i = 2
    k = 0
    while i < question:
        if question % i == 0:
            k += 1
        i += 1
    if k == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (question, correct_answer)
