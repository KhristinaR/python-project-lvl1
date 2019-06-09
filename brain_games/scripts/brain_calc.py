from brain_games.games.games_functions import welcome_text, random_values, operate_numbers, congrat_text
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
       operator = random_values()[1]
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
