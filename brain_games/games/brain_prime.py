import random


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_answer(num):

    i = 2
    while(i < num):
        if num % i == 0:
            return 'no'
        i = i + 1
    return 'yes'


def question():

    num = random.randint(1, 100)
    question = "{} {} {}".format('Question:', num, '')
    correct_answer = get_answer(num)
    return (question, correct_answer)
