from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        num1 = randint(1, 25)
        num2 = randint(1, 25)
        operand_type = randint(1, 3)
        if operand_type == 1:
            print(f'Question: {num1} + {num2}')
            cor_res = num1 + num2
        elif operand_type == 2:
            print(f'Question: {num1} - {num2}')
            cor_res = num1 - num2
        else:
            print(f'Question: {num1} * {num2}')
            cor_res = num1 * num2
        answer = prompt.string('Your answer: ')
        try:
            ans = int(answer)
        except ValueError:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{cor_res}'.'")
            print(f"Let's try again, {name}!")
            break
        if ans == cor_res:
            print('Correct!')
            i += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_res}'.'")
            print(f"Let's try again, {name}!")
            break
        if i >= 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
