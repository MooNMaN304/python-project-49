import random


RULE = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 30
OPERATOR = ['*', '-', '+']


def result_and_question():
    first_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    math_operation = random.choice(OPERATOR)
    if math_operation == '+':
        result = first_num + second_num
    if math_operation == '-':
        result = first_num - second_num
    if math_operation == '*':
        result = first_num * second_num
    question = f'{first_num} {math_operation} {second_num}'
    return str(result), question
