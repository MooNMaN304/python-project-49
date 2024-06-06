from brain_games.tools.random_number import number
from brain_games.tools.data import generate_game_data
from brain_games.tools.round_tools import SIGNS


def calco1():
    number1 = number(1, 30)
    number2 = number(1, 30)
    rules = SIGNS.pop()
    question = f'{number1} {rules} {number2}'
    result = eval(question)
    return str(result), question


def calco2():
    rules = "What is the result of the expression?"
    generate_game_data(calco1, rules)
