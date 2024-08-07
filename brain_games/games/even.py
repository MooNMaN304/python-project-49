import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number):
    return (number % 2 == 0)


def generate_game_data():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(question) is True:
        result = 'yes'
    else:
        result = 'no'
    return result, str(question)
