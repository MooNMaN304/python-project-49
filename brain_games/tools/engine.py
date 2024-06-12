import prompt


def generate_game_data(result_question_rules):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name} !")
    result, question, RULES = result_question_rules()
    print(RULES)
    win = 0
    while win < 3:
        result, question, RULES = result_question_rules()
        print("Question: " + question)
        answer = prompt.string('Your answer: ')
        if answer == result:
            win += 1
            if win == 3:
                print(f"Congratulations, {name}!")
                break
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{result}'."
            )
            print(f"""Let's try again, {name}!""")
            break
