import prompt
from brain_games.tools.welcome import welcome_user
from brain_games.tools.random_number import special_number
from brain_games.tools.round_script import round_number


def if_del():
  win = 0
  name = welcome_user()
  print ("""Answer "yes" if given number is prime. Otherwise answer "no".""")
  while win < 3:
    if win == -404:
      break
    box = []
    number1 = special_number(2, 100)
    for i in range(number1):
      if number1 % (i + 1) == 0:
        box += [i+1]
    if len(box) == 2:
      result = "yes"
    else:
      result = "no"
    print (f"""Question: {number1}""")
    answer = prompt.string('Your answer: ')
    win = round_number(name, result, answer, win)
