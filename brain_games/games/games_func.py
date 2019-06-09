import random
import prompt

def is_number_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'

def operate_numbers(num_1, operator, num_2):
    if operator == '+':
        result = int(num_1) + int(num_2)
    elif operator == '-':
        result = int(num_1) - int(num_2)
    elif operator == '*':
        result =  int(num_1) * int(num_2)
    return str(result)

def welcome_text():
    print('Welcome to the Brain Games!')

def greeting():
    name = prompt.string('May I have your name? ')
    greeting = "{}, {}{}".format('Hello', name, '!')
    print(greeting)

def congrat_text(name):
    print('{}, {}{}'.format('Congratulations', name, '!'))

def even_questions():
    number = random.randint(1, 1000)
    return number

def calc_questions():
    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    operators = ('+', '-', '*')
    operator = random.choice(operators)
    questions = (num_1, operator, num_2)
    return questions


