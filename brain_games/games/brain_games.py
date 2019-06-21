from brain_games.engine.cli import welcome, greeting
import prompt


def demo():

    welcome()
    name = prompt.string('May I have your name? ')
    greeting(name)
