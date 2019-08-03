def welcome():
    print('Welcome to the Brain Games!')


def congrat(name):
    print('Congratulations, {}!'.format(name))


def show_error(user_answer, correct_answer, name):
    print("{} is wrong answer ;(. Correct answer was {}."
          .format(user_answer, correct_answer))
    print("Let's try again, {}!".format(name))


def greet(name):
    print("Hello, {}!".format(name))
