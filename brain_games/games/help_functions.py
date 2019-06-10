import random


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
        result = int(num_1) * int(num_2)
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


def progression_calc():
    step = random.randint(1, 10)
    random_number = random.randint(1, 1000)
    i = 0
    progression = ''
    random_step = random.randint(0, 9)
    hidden_number = 0
    while(i <= 11):
        if(i == random_step):
            progression = progression + ' ' + '..'
            hidden_number = str(random_number)
            random_number = random_number + step
            i = i + 1
        else:
            progression = progression + ' ' + str(random_number)
            random_number = random_number + step
            i = i + 1
    results = (progression, hidden_number)
    return results


def is_prime_number(num):
    i = 2
    while(i < num):
        if num % i == 0:
            return 'no'
        i = i + 1
    return 'yes'


def error_text(user_answer, correct_answer, name):
    str_1 = "is wrong answer ;(. Correct answer was "
    str_2 = "{}, {}!".format("Let's try again", name)
    error_text = "{} {}{}.".format(user_answer, str_1, correct_answer)
    print(error_text)
    print(str_2)
