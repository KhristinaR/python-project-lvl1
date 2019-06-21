import random


INSTRUCTION = 'Answer "yes" if number even otherwise answer "no".'

num = random.randint(1, 1000)


def get_answer(num):

    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def question():

    num = random.randint(1, 100)
    question = "{} {} {}".format('Question:', num, '')
    correct_answer = get_answer(num)
    return (question, correct_answer)
