from brain_games.engine.cli import welcome, greet, show_error, congrat
import prompt


def engine(game):
    welcome()
    print(game.INSTRUCTION)
    name = prompt.string('May I have your name? ')
    greet(name)
    rounds = 3
    while rounds:
        (question, correct_answer) = game.generate_question()
        user_answer = prompt.string(question)
        if user_answer == correct_answer:
            print("Correct!")
            rounds = rounds - 1
        else:
            show_error(user_answer, correct_answer, name)
            exit()

    congrat(name)
