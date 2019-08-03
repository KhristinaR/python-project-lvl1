import random

INSTRUCTION = 'What is the result of the expression?'


def get_answer(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    else:
        raise ValueError("Either the operator or numbers are not correct!")
    return result


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operators = ('+', '-', '*')
    operator = random.choice(operators)
    question = "Question: {} {} {}".format(num1, operator, num2)
    correct_answer = str(get_answer(num1, operator, num2))
    return (question, correct_answer)
