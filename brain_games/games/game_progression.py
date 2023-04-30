from random import randint

GAME_RULE = 'What number is missing in the progression?'


def generate_progression():
    start = randint(1, 10)
    step = randint(2, 5)
    length = randint(5, 10)
    list = []
    num = start
    index = 0
    while index < length:
        list.append(num)
        num += step
        index += 1
    return list


def get_game():
    progression = generate_progression()
    missing_number = randint(0, len(progression) - 1)
    correct_answer = progression[missing_number]
    question = ""
    for number in progression:
        if number == correct_answer:
            question += ".. "
        else:
            question += str(number) + " "
    question = question.strip()
    return question, correct_answer
