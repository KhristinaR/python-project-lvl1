def welcome():

    print('Welcome to the Brain Games!')


def congrat(name):

    print('{}, {}{}'.format('Congratulations', name, '!'))


def error(user_answer, correct_answer, name):

    str_1 = "is wrong answer ;(. Correct answer was "
    str_2 = "{}, {}!".format("Let's try again", name)
    error_text = "{} {}{}.".format(user_answer, str_1, correct_answer)
    print(error_text)
    print(str_2)


def greeting(name):

    result = "{}, {}{}".format('Hello', name, '!')
    print(result)
