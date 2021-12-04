import random


def user_input():
    guess = str(input('Enter your guess: '))
    return guess


guess = ''

masternum = ''
for i in range(4):
    masternum = masternum + str((random.randrange(0, 10)))
split_masternum = list(masternum)

while guess != masternum:
    guess = user_input()
    if len(guess) > 4 or len(guess) < 4:
        print('guess must be 4 numbers long')
        continue
    split_guess = list(guess)






