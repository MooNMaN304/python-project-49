import prompt
from brain_games.tools.welcome import welcome_user



def generate_game_data(result_and_question, rules):
    name = welcome_user()
    print (rules)
    win = 0
    while win < 3:
        result, question = result_and_question()
        print ("Question: " + question)
        answer = prompt.string('Your answer: ')
        if answer == result:
            win += 1
            if win == 3:
                print(f"Congratulations, {name}!")
                break
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"""Let's try again, {name}!""")
            break
