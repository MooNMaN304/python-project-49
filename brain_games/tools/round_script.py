def round_number(name, result, answer, win):
  if int(answer) == result:
    print("Correct!")
    win += 1
    if win == 3:
      print(f"Congratulations, {name}!")
      return win
    return win
  else:
    print(
        f"""'{answer}'is wrong answer ;(.Correct answer was '{result}'.Let's try again, {name}!"""
    )
    win = -404
    return win
