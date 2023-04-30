import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULE)
    round_counter = 0
    while round_counter < 3:
        question, corr = game.get_game()
        print('Question:', question)
        answ = prompt.string('Your answer: ')
        if str(answ) == str(corr):
            print('Correct!')
            round_counter = round_counter + 1
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{corr}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
