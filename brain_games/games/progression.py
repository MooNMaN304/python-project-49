import random


def progress1():
    box = []
    progressive_lenght = 10
    start = random.randint(1, 20)
    step = random.randint(1, 20)
    steal_number = random.randint(0, 9)
    for i in range(progressive_lenght):
        start += step
        box += [start]
    result = box[steal_number]
    box[steal_number] = ".."
    question = " ".join(map(str, box))
    return str(result), question
