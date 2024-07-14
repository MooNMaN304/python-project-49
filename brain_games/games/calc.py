import random


RULE = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 30
OPERATORS = ['*', '-', '+']


def generate_game_data():
    first_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATORS)
    if operator == '+':
        result = first_num + second_num
    if operator == '-':
        result = first_num - second_num
    if operator == '*':
        result = first_num * second_num
    question = f'{first_num} {operator} {second_num}'
    return str(result), question
