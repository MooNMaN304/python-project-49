import random


MIN_NUMBER_GAME = 1
MAX_NUMBER_GAME = 100


def del_of_two():
    RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = random.randint(MIN_NUMBER_GAME, MAX_NUMBER_GAME)
    if question % 2 == 0:
        result = "yes"
    else:
        result = "no"
    return result, str(question), RULE
