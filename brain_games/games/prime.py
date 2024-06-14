import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 2
MAX_NUMBER = 100


def is_prime(number):
    for i in range(number - 2):
        if number % (i + 2) == 0:
            return False
    return True


def result_and_question():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(question) is True:
        result = "yes"
    else:
        result = "no"
    return result, str(question)
