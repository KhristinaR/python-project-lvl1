from brain_games.games.games_func import welcome_text, greeting, even_questions as question_number, is_number_even, congrat_text
import prompt


def main():
    welcome_text()
    name = prompt.string('May I have your name? ')
    greeting = "{}, {}{}".format('Hello', name, '!')
    print(greeting)
    i = 0
    while (i <= 2):
       number = question_number()
       question_text = "{} {} {}".format('Question:',number, '')
       user_answer = prompt.string(question_text)
       correct_answer = is_number_even(number)
       if user_answer == correct_answer:
           print("Correct!")
           i = i + 1
       else:
           error_text = "{} {}{}.{}, {}{}".format(user_answer, "is wrong answer ;(. Correct answer was ", correct_answer, "\nLet's try again", name, "!")
           print(error_text)
           exit()
    congrat_text(name)

main()
