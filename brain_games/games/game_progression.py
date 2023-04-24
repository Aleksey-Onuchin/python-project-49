from random import randint

GAME_RULE = 'What number is missing in the progression?'


def get_game():
    list = generate_progression()
    missing_char = randint(0, len(list) - 1)
    correct_answer = list[missing_char]
    question = ""
    for i in list:
        if i == correct_answer:
            question += ".. "
        else:
            question += str(i) + " "
    question = question.strip()
    return question, correct_answer


def generate_progression():
    start = randint(1, 10)
    step = randint(2, 5)
    length = randint(5, 10)
    list = []
    num = start
    i = 0
    while i < length:
        list.append(num)
        num += step
        i += 1
    return list
