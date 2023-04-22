from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        num1 = randint(1, 50)
        num2 = randint(1, 50)
        operand_type = randint(1, 3)
        if operand_type == 1:
            print(f'Question: {num1} + {num2}')
            correct_result = num1 + num2
        elif operand_type == 2:
            print(f'Question: {num1} - {num2}')
            correct_result = num1 - num2
        else:
            print(f'Question: {num1} * {num2}')
            correct_result = num1 * num2
        ans = int(prompt.string('Your answer: '))
        if ans == correct_result:
            print('Correct!')
            i += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{correct_result}'.'")
            print(f"Let's try again, {name}!")
            break
        if i >= 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()