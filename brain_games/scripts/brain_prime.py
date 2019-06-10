import prompt
from brain_games.games.help_functions import welcome_text, congrat_text
from brain_games.games.help_functions import is_prime_number, random_values
from brain_games.games.help_functions import error_text


def main():

    welcome_text()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = prompt.string('May I have your name? ')
    greeting = "{}, {}{}".format('Hello', name, '!')
    print(greeting)
    i = 0
    while (i <= 2):
        number = random_values()[0]
        question_text = "{} {} {}".format('Question:', number, '')
        user_answer = prompt.string(question_text)
        correct_answer = is_prime_number(number)
        if user_answer == correct_answer:
            print("Correct!")
            i = i + 1
        else:
            error_text(user_answer, correct_answer, name)
            exit()

    congrat_text(name)
