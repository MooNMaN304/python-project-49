import random


MIN_NUMBER_GAMES = 1
MAX_NUMBER_GAMES = 30
SIGNS = ["*", "-", "+"]


def calc():
    RULE = "What is the result of the expression?"
    first_num = random.randint(MIN_NUMBER_GAMES, MAX_NUMBER_GAMES)
    second_num = random.randint(MIN_NUMBER_GAMES, MAX_NUMBER_GAMES)
    math_sign = random.choice(SIGNS)
    if math_sign == "+":
        result = first_num + second_num
    if math_sign == "-":
        result = first_num - second_num
    if math_sign == "*":
        result = first_num * second_num
    question = f'{first_num} {math_sign} {second_num}'
    return str(result), question, RULE
