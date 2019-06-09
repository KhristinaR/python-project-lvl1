from brain_games.games.games_func import welcome_text, greeting, calc_questions, operate_numbers, congrat_text
import prompt


def main():
    welcome_text()
    name = prompt.string('May I have your name? ')
    greeting = "{}, {}{}".format('Hello', name, '!')
    print(greeting)
    i = 0
    while (i <= 2):
       num_1 = calc_questions()[0]
       num_2 = calc_questions()[2]
       operator = calc_questions()[1]
       question_text = "{} {} {} {} {}".format('Question:',num_1, operator, num_2, '')
       user_answer = prompt.string(question_text)
       correct_answer = operate_numbers(num_1, operator, num_2)
       if user_answer == correct_answer:
           print("Correct!")
           i = i + 1
       else:
           error_text = "{} {}{}.{}, {}{}".format(user_answer, "is wrong answer ;(. Correct answer was ", correct_answer, "\nLet's try again", name, "!")
           print(error_text)
           exit()
    congrat_text(name)

main()
