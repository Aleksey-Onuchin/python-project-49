import prompt


def main(game, task):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(task)
    i = 0
    while i < 3:
        question, corr = game()
        print('Question:', question)
        answ = prompt.string('Your answer: ')
        if str(answ) == str(corr):
            print('Correct!')
            i = i + 1
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{corr}'.")
            print(f"Let's try again, {name}!")
            break
        if i == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
