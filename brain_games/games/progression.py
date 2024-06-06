from brain_games.tools.random_number import number
from brain_games.tools.data import generate_game_data
from brain_games.tools.round_tools import beatiful_question


def progress1():
    box = []
    number1 = number(1, 20)
    number2 = number(1, 20)
    steal = number(0, 9)
    for i in range(10):
        number1 += number2
        box += [number1]
    result = box[steal]
    box[steal] = [".."]
    question = beatiful_question(box)
    return str(result), question


def progress2():
    rules = "What number is missing in the progression?"
    generate_game_data(progress1, rules)
