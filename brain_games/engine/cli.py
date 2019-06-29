def welcome():
    print('Welcome to the Brain Games!')


def congrat(name):
    print('Congratulations, {}!'.format(name))


def show_error(user_answer, correct_answer, name):
    try_again_text = "Let's try again, {}!".format(name)
    wrong_text = " is wrong answer ;(. Correct answer was "
    error_text = "{}{}{}.".format(user_answer, wrong_text, correct_answer)
    try_again_text = "{}, {}!".format("Let's try again", name)
    print(error_text)
    print(try_again_text)


def greet(name):
    result = "{}, {}{}".format('Hello', name, '!')
    print(result)
