import random
import math

INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_answer(num):
    divisor = 2
    while divisor <= math.sqrt(num):
        if num % divisor:
            divisor = divisor + 1
        else:
            return 'no'
    return "yes"


def generate_question():
    num = random.randint(1, 100)
    question = "{} {} ".format('Question:', num)
    correct_answer = get_answer(num)
    return (question, correct_answer)
