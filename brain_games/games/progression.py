import random


MIN_STEP = 1
MAX_STEP = 20
PROGRESSIVE_LENGHT = 10
MIN_HIDDEN_NUMBER = 0
MAX_HIDDEN_NUMBER = 9


def progress():
    RULE = "What number is missing in the progression?"
    box = []
    start = random.randint(MIN_STEP, MAX_STEP)
    step = random.randint(MIN_STEP, MAX_STEP)
    steal_number = random.randint(MIN_HIDDEN_NUMBER, MAX_HIDDEN_NUMBER)
    for i in range(PROGRESSIVE_LENGHT):
        start += step
        box += [start]
    result = box[steal_number]
    box[steal_number] = ".."
    question = " ".join(map(str, box))
    return str(result), question, RULE
