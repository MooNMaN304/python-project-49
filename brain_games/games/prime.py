import random


def if_del1():
    box = []
    number1 = random.randint(2, 100)
    for i in range(number1):
        if number1 % (i + 1) == 0:
            box += [i + 1]
    if len(box) == 2:
        result = "yes"
    else:
        result = "no"
    question = str(number1)
    return result, question
