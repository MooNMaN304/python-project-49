#!/usr/bin/env python3


import prompt
import random
from brain_games.welcome import welcome_user


def even_or_no():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    win = 0
    while win <= 2:
        number = random.randint(1, 100)
        print ("Question: " + str(number))
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            result = "yes"
        if number % 2 != 0:
            result = "no"
        if result == answer:
            if win == 2:
                print ('Congratulations, ' + name + '!')
                break
            else:
                print ("Correct!")
                win += 1
        else:
             print (f"""'{answer}' is wrong answer ;(. Correct answer was '{result}'.Let's try again, {name}!""")
             break


def main():
    even_or_no()


if __name__ == "__main__":
    main()
