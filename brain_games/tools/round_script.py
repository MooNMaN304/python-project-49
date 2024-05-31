def round_number(name, result, answer, win):
    if answer == result:
        print("Correct!")
        win += 1
        if win == 3:
            print(f"Congratulations, {name}!")
            return win
        return win
    else:
        print(f"""'{answer}'is wrong answer ;(. Correct answer was '{result}'.""")
        print(f"""Let's try again, {name}!""")
        win = -404
        return win


def beatiful_question(text):
    abs1 = ""
    for i in text:
        abs1 += str(i) + " "
    j = 0
    beatiful_result = ""
    while j <= len(abs1) - 1:
        if abs1[j] == "[":
            beatiful_result += ""
            j += 1
        if abs1[j] == "]":
            beatiful_result += ""
            j += 1
        if abs1[j] == "'":
            beatiful_result += ""
            j += 1
        else:
            beatiful_result += abs1[j]
            j += 1
    return beatiful_result
