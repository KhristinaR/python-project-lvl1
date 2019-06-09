import random

def is_number_even(num):
    if num % 2:
        return 'yes'
    else:
        return 'no'

def sum_numbers(num1, num2):
    result = num1 + num2
    return result

def welcome_text:
    print('Welcome to the Brain Games!')

def question_text:
    print("{} {} ".format('Question:',questions[i], ''))
    answer = prompt.string(question_text)
    return answer

def greeting:
    name = prompt.string('May I have your name? ')
    greeting = "{}, {}{}".format('Hello', name, '!')
    print(greeting)

def even_questions:
    question_1 = random.randint(1, 1000)
    question_2 = random.randint(1, 1000)
    questions_3 = random.randint(1, 1000)
    questions = (question_1, question_2, question_3)
    return questions

def calc_questions:
    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    questions = (num_1, num_2)
    return questions
