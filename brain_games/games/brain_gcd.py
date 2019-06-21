import random


INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def get_answer(num_1, num_2):

    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    result = num_1 + num_2
    return str(result)


def question():

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    question = "{} {} {} {}".format('Question:', num_1, num_2, '')
    correct_answer = get_answer(num_1, num_2)
    return (question, correct_answer)
