import random


INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    while num1 and num2:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    result = num1 + num2
    return result


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = "Question: {} {}".format(num1, num2)
    correct_answer = get_gcd(num1, num2)
    return (question, str(correct_answer))
