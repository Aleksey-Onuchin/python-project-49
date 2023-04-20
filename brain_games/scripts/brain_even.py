from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        num = randint(1, 20)
        print('Question: ', num)
        ans = prompt.string('Your answer: ')
        if num % 2 == 0 and ans == 'yes' or num % 2 != 0 and ans == 'no':
            print('Correct!')
            i += 1
        else:
            c_ans = 'yes' if num % 2 == 0 else 'no'
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{c_ans}'.'")
            print(f"Let's try again, {name}!")
            break
        if i >= 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
