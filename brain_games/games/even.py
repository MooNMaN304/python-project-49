import random


def del_of_two1():
    question = random.randint(1, 100)
    if question % 2 == 0:
        result = "yes"
    else:
        result = "no"
    return result, str(question)
