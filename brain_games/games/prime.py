from brain_games.tools.random_number import number
from brain_games.tools.data import generate_game_data


def if_del1():
    box = []
    number1 = number(1, 100)
    for i in range(number1):
      if number1 % (i + 1) == 0:
        box += [i + 1]
    if len(box) == 2:
      result = "yes"
    else:
      result = "no"
    question = f'{number1}'
    return result, question 


def if_del2():
    rules = f'Answer "yes" if given number is prime. Otherwise answer "no".'
    generate_game_data(if_del1, rules)
