from brain_games.games.help_functions import welcome_text, random_values
from brain_games.games.help_functions import operate_numbers, congrat_text
from brain_games.games.help_functions import error_text
import prompt


def main():

    welcome_text()
    print('What is the result of the expression?')
    name = prompt.string('May I have your name? ')
    greeting = "{}, {}{}".format('Hello', name, '!')
    print(greeting)
    i = 0
    while (i <= 2):
        num_1 = random_values()[0]
        num_2 = random_values()[2]
        operat = random_values()[1]
        q_text = "{} {} {} {} {}".format('Question:', num_1, operat, num_2, '')
        user_answer = prompt.string(q_text)
        correct_answer = operate_numbers(num_1, operat, num_2)
        if user_answer == correct_answer:
            print("Correct!")
            i = i + 1
        else:
            error_text(user_answer, correct_answer, name)
            exit()

    congrat_text(name)
