import prompt


GAME_COUNT = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name} !')
    print(game.RULE)
    for round in range(GAME_COUNT):
        result, question = game.generate_game_data()
        print(f'Question:  {question}')
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print(
                f'"{answer}" is wrong answer ;(.'
                f' Correct answer was "{result}".\n'
                f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
