import random


INSTRUCTION = 'Answer "yes" if number even otherwise answer "no".'


def get_answer(num):
    if num % 2:
        return 'no'
    else:
        return 'yes'


def generate_question():
    num = random.randint(1, 100)
    question = "{} {} ".format('Question:', num)
    correct_answer = get_answer(num)
    return (question, correct_answer)
