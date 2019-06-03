import prompt

def run():
    name = prompt.string('May I have your name? ')
    greeting = "{},{}{}".format('Hello',name,'!')
    print(greeting)
