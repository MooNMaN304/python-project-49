import random


MIN_NUMBER_GAME = 2
MAX_NUMBER_GAME = 100


def is_prime(number):
    box = []
    for i in range(number):
        if number % (i + 1) == 0:
            box += [i + 1]
    if len(box) == 2:
        return True
    else:
        return False


def prime():
    RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = random.randint(MIN_NUMBER_GAME, MAX_NUMBER_GAME)
    if is_prime(question) is True:
        result = "yes"
    else:
        result = "no"
    return result, str(question), RULE
