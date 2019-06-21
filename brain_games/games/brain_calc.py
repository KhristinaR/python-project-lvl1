import random

INSTRUCTION = 'What is the result of the expression?'


def get_answer(num_1, operator, num_2):

    if operator == '+':
        result = int(num_1) + int(num_2)
    elif operator == '-':
        result = int(num_1) - int(num_2)
    elif operator == '*':
        result = int(num_1) * int(num_2)
    return str(result)


def question():

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    operators = ('+', '-', '*')
    operator = random.choice(operators)
    question = "{} {} {} {} {}".format('Question:', num_1, operator, num_2, '')
    correct_answer = get_answer(num_1, operator, num_2)
    return (question, correct_answer)
