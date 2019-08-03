import random
import math

INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    divisor = 2
    while divisor <= math.sqrt(num):
        if num % divisor:
            divisor = divisor + 1
        else:
            return True
    return False


def generate_question():
    num = random.randint(1, 100)
    question = "Question: {}".format(num)
    correct_answer = "no" if is_prime(num) else "yes"
    return (question, correct_answer)
