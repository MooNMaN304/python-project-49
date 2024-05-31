import prompt
from brain_games.tools.welcome import welcome_user
from brain_games.tools.random_number import special_number
from brain_games.tools.round_script import round_number
from brain_games.tools.round_script import beatiful_question


def progress():
  win = 0
  name = welcome_user()
  while win < 3:
    if win == -404:
      break
    box = []
    number1 = special_number(1, 20)
    number2 = special_number(1, 20)
    steal = special_number(0, 9)
    for i in range(10):
      number1 += number2
      box += [number1]
    result = box[steal]
    box[steal] = [".."]
    question = beatiful_question(box)
    print ("What number is missing in the progression?")
    print (f"Question: {question}")
    answer = prompt.string('Your answer: ')
    win = round_number(name, str(result), answer, win)
