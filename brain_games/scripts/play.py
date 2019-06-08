import prompt


def play(questions):
    welcome_text = '''Welcome to the Brain Games! 
Answer 'yes' if number even otherwise answer 'no'.
    '''
    print(welcome_text)
    name = prompt.string('May I have your name? ')
    greeting = "{}, {}{}".format('Hello', name, '!')
    print(greeting)
    i = 0
    while (i <= 2):
       question_text = "{} {} ".format('Question:',questions[i], '')
       answer = prompt.string(question_text)
       if(questions[i] % 2 == 0) & (answer == 'yes'):
           print("Correct!")
           i = i + 1
       elif(questions[i] % 2) == 0 & (answer != 'yes'):
           error_yes_text = "{} {}, {}{}".format(answer, "is wrong answer ;(. Correct answer was 'yes'.\nLet's try again", name, '!')
           print(error_yes_text)
       elif(questions[i] % 2 != 0) & (answer == 'no'):
           print("Correct!")
           i = i + 1
       elif(questions[i] % 2 != 0) & (answer != 'no'):
           error_no_text = "{} {}, {}{}".format(answer, "is wrong answer ;(. Correct answer was 'no'.\nLet's try again", name, '!')
           print(error_no_text)
    congrat_text ="{}, {}{}".format("Congratulations", name, '!')
    print(congrat_text)
