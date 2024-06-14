import prompt


GAME_ROUNDS = 3


def generate_game_data(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name} !')
    print(game.RULE)
    for round in range(GAME_ROUNDS):
        result, question = game.result_and_question()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
            if round == 2:
                print(f'Congratulations, {name}!')
        else:
            print(
                f'"{answer}" is wrong answer ;(. Correct answer was "{result}".'
            )
            print(f'Let\'s try again, {name}!')
            break
