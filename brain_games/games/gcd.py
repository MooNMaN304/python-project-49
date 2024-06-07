import random


def big_del1():
    result_del = []
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    for i in range(min(number1, number2)):
        if min(number1, number2) % (i + 1) == 0:
            if max(number1, number2) % (i + 1) == 0:
                result_del += [(i + 1)]
    question = f'{number1} {number2}'
    result = max(result_del)
    return str(result), question
