from brain_games.tools.random_number import number
from brain_games.tools.data import generate_game_data


def big_del1():
    result_del = []
    number1 = number(1, 100)
    number2 = number(1, 100)
    for i in range(min(number1, number2)):
      if min(number1, number2) % (i + 1) == 0:
        if max(number1, number2) % (i + 1) == 0:
          result_del += [(i + 1)]
    question = f'{number1} {number2}'
    result = max(result_del)
    return str(result), question

def big_del2():
    rules = f"Find the greatest common divisor of given numbers."
    generate_game_data(big_del1, rules)
