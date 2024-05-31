import prompt
from brain_games.tools.welcome import welcome_user
from brain_games.tools.random_number import number
from brain_games.tools.round_script import round_number

def del_of_two():
  name = welcome_user()
  print('Answer "yes" if the number is even, otherwise answer "no".')
  win = 0
  while win < 3:
    if win == -404:
      break
    number1 = number()
    if number1 % 2 == 0:
      result = "yes"
    if number1 % 2 != 0:
      result = "no"
    print("Question: " + str(number1))
    answer = prompt.string('Your answer: ')
    win = round_number(name, result, answer, win)
