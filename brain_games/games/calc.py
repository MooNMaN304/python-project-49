import prompt
from brain_games.tools.welcome import welcome_user
from brain_games.tools.random_number import number
from brain_games.tools.round_script import round_number


def calco():
    win = 0
    name = welcome_user()
    options = ["+", "-", "*"]
    print("What is the result of the expression?")
    while win < 3:
        number1 = number()
        number2 = number()
        result = [(number1 + number2), (number1 - number2), (number1 * number2)]
        if win == -404:
            break
        print(f"""Question: {number1} {options[win]} {number2}""")
        answer = prompt.string('Your answer: ')
        win = round_number(name, str(result[win]), answer, win)
