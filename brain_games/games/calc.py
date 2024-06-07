import random
from brain_games.tools.round_tools import SIGNS


def calco1():
    number1 = random.randint(1, 30)
    number2 = random.randint(1, 30)
    rules = SIGNS.pop()
    question = f'{number1} {rules} {number2}'
    result = eval(question)
    return str(result), question
