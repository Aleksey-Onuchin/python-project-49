from random import randint

task = 'What number is missing in the progression?'


def progression():
    start = randint(1, 10)
    step = randint(2, 5)
    length = randint(5, 10)
    missing_char = randint(5, length)
    list = []
    num = start
    i = 0
    while i < length:
        list.append(num)
        num += step
        i += 1
    correct_answer = list[missing_char - 1]
    question = ""
    for i in list:
        if i == correct_answer:
            question += ".. "
        else:
            question += str(i) + " "
    return (question, correct_answer)
