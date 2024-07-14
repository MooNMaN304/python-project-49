import random


RULE = 'What number is missing in the progression?'
MIN_STEP = 1
MAX_STEP = 20
PROGRESSIVE_LENGTH = 10
MIN_HIDDEN = 0
MAX_HIDDEN = 9


def generate_game_data():
    progression = []
    start = random.randint(MIN_STEP, MAX_STEP)
    step = random.randint(MIN_STEP, MAX_STEP)
    steal_number = random.randint(MIN_HIDDEN, MAX_HIDDEN)
    for i in range(PROGRESSIVE_LENGTH):
        start += step
        progression += [start]
    result = progression[steal_number]
    progression[steal_number] = ".."
    question = " ".join(map(str, progression))
    return str(result), question
