import random


INSTRUCTION = 'What number is missing in the progression?'


def generate_question():
    step = random.randint(1, 10)
    random_number = random.randint(1, 1000)
    counter = 0
    progression = ''
    random_step = random.randint(0, 9)
    chunk = ''
    while counter <= 11:
        if counter == random_step:
            chunk = '..'
            correct_answer = str(random_number)
        else:
            chunk = str(random_number)
        progression += ' ' + chunk
        random_number = random_number + step
        counter = counter + 1
    question = "Question: {}".format(progression.lstrip())
    results = (question, correct_answer)
    return results
