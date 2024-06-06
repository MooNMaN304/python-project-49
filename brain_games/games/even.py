from brain_games.tools.random_number import number
from brain_games.tools.data import generate_game_data


def del_of_two1():
    number1 = number(1, 100)
    if number1 % 2 == 0:
        result = "yes"
    if number1 % 2 != 0:
        result = "no"
    question = f"Question: {number1}"
    return result, question


def del_of_two2():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    generate_game_data(del_of_two1, rules)
