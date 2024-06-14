import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def del_of_two(number):
    return (number % 2 == 0)


def result_and_question():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    if del_of_two(question) is True:
        result = 'yes'
    else:
        result = 'no'
    return result, str(question)
