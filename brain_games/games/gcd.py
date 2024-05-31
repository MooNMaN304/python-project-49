import prompt
from brain_games.tools.welcome import welcome_user
from brain_games.tools.random_number import number
from brain_games.tools.round_script import round_number


def big_del():
  win = 0
  name = welcome_user()
  while win < 3:
    result_del = []
    numb_del1 = []
    numb_del2 = []
    if win == -404:
      break
    number1 = number()
    number2 = number()
    for i in range(number1):
      if number1 % (i + 1) == 0:
        numb_del1 += [(i + 1)]
    for j in range(number2):
      if number2 % (j + 1) == 0:
        numb_del2 += [(j + 1)]
    for x in numb_del1:
      for y in numb_del2:
        if x == y:
          result_del += [x]
    print(f"""Question: {number1} {number2}""")
    answer = prompt.string('Your answer: ')
    result = max(result_del)
    win = round_number(name, str(result), answer, win)
