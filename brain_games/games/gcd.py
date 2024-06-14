import random
import math


RULE = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def result_and_question():
    first_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{first_num} {second_num}'
    result = math.gcd(first_num, second_num)
    return str(result), question
