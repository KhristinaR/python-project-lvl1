import prompt
from brain_games.games.help_functions import welcome_text, congrat_text
from brain_games.games.help_functions import progression_calc
from brain_games.games.help_functions import error_text


def main():

    welcome_text()
    print('What number is missing in the progression?')
    name = prompt.string('May I have your name? ')
    greeting = "{}, {}{}".format('Hello', name, '!')
    print(greeting)
    i = 0
    progressions = progression_calc()
    correct_answer = progressions[1]
    progression = progressions[0]
    while (i <= 2):
        progressions = progression_calc()
        correct_answer = progressions[1]
        progression = progressions[0]
        question_text = "{} {} {}".format('Question:', progression, '')
        user_answer = prompt.string(question_text)
        if user_answer == correct_answer:
            print("Correct!")
            i = i + 1
        else:
            error_text(user_answer, correct_answer, name)
            exit()

    congrat_text(name)
