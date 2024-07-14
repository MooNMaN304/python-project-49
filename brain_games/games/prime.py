import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 100


def is_prime(number):
    if (number == 0) or (number == 1):
        return False
    for i in range(number - 2):
        if number % (i + 2) == 0:
            return False
    return True


def generate_game_data():
    game_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = game_num
    if is_prime(game_num) is True:
        result = 'yes'
    else:
        result = 'no'
    return result, str(question)
