from brain_games.engine.cli import welcome, greeting, error, congrat
import prompt


def engine(game):

    welcome()
    print(game.INSTRUCTION)
    name = prompt.string('May I have your name? ')
    greeting(name)
    i = 0
    while (i <= 2):
        (question, correct_answer) = game.question()
        user_answer = prompt.string(question)
        if user_answer == correct_answer:
            print("Correct!")
            i = i + 1
        else:
            error(user_answer, correct_answer, name)
            exit()

    congrat(name)
