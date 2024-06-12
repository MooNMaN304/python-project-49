import random
import math


MIN_NUMBER_GAMES = 1
MAX_NUMBER_GAMES = 100


def big_del():
    RULE = "Find the greatest common divisor of given numbers."
    first_num = random.randint(MIN_NUMBER_GAMES, MAX_NUMBER_GAMES)
    second_num = random.randint(MIN_NUMBER_GAMES, MAX_NUMBER_GAMES)
    question = f'{first_num} {second_num}'
    result = math.gcd(first_num, second_num)
    return str(result), question, RULE
