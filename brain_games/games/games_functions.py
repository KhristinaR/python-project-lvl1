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

def congrat_text(name):
    print('{}, {}{}'.format('Congratulations', name, '!'))

def calc_questions():
    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    operators = ('+', '-', '*')
    operator = random.choice(operators)
    questions = (num_1, operator, num_2)
    return questions


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

def congrat_text(name):
    print('{}, {}{}'.format('Congratulations', name, '!'))

def random_values():
    number_1 = random.randint(1, 1000)
    number_2 = random.randint(1, 1000)
    operators = ('+', '-', '*')
    operator = random.choice(operators)
    result = (number_1, operator, number_2)
    return result

def find_gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    result = num_1 + num_2
    return str(result)

