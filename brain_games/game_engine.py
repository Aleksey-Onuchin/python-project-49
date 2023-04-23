import prompt


def main(game, task):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(task)
    i = 0
    while i < 3:
        question, correct_answer = game()
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        if str(answer) == str(correct_answer):
            print('Correct!')
            i += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.'")
            print(f"Let's try again, {name}!")
            break
        if i == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
