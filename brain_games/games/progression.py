import random


RULE = 'What number is missing in the progression?'
MIN_STEP = 1
MAX_STEP = 20
PROGRESSIVE_LENGHT = 10
MIN_HIDDEN_NUM = 0
MAX_HIDDEN_NUM = 9


def result_and_question():
    box = []
    start = random.randint(MIN_STEP, MAX_STEP)
    step = random.randint(MIN_STEP, MAX_STEP)
    steal_number = random.randint(MIN_HIDDEN_NUM, MAX_HIDDEN_NUM)
    for i in range(PROGRESSIVE_LENGHT):
        start += step
        box += [start]
    result = box[steal_number]
    box[steal_number] = ".."
    question = " ".join(map(str, box))
    return str(result), question
