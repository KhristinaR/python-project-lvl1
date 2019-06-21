import random


INSTRUCTION = 'What number is missing in the progression?'


def question():

    step = random.randint(1, 10)
    random_number = random.randint(1, 1000)
    i = 0
    progression = ''
    random_step = random.randint(0, 9)
    while(i <= 11):
        if(i == random_step):
            progression = progression + ' ' + '..'
            correct_answer = str(random_number)
            random_number = random_number + step
            i = i + 1
        else:
            progression = progression + ' ' + str(random_number)
            random_number = random_number + step
            i = i + 1
    question = "{} {} {}".format('Question:', progression, '')
    results = (question, correct_answer)
    return results
