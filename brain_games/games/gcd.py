import prompt
from brain_games.tools.welcome import welcome_user
from brain_games.tools.random_number import number
from brain_games.tools.round_script import round_number


def big_del():
    win = 0
    name = welcome_user()
    while win < 3:
        result_del = []
        if win == -404:
            break
        number1 = number()
        number2 = number()
        for i in range(min(number1, number2)):
            if min(number1, number2) % (i + 1) == 0:
                if max(number1, number2) % (i + 1) == 0:
                    result_del += [(i + 1)]
        print(f"""Question: {number1} {number2}""")
        answer = prompt.string('Your answer: ')
        result = max(result_del)
        win = round_number(name, str(result), answer, win)
