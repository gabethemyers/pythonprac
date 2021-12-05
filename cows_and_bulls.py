import random


def user_input():
    guess = str(input('Enter your guess: '))
    return guess


guess = ''
cow_count = 0
masternum = ''

split_masternum = list(masternum)

for i in range(4):
    masternum = masternum + str((random.randrange(0, 10)))


while guess != masternum:
    guess = user_input()
    if len(guess) > 4 or len(guess) < 4:
        print('guess must be 4 numbers long')
        continue
    split_guess = list(guess)
    maybe_bulls = split_guess.copy()

    for inx, ele in enumerate(split_guess):
        if ele == masternum[inx]:
            cow_count += 1
            maybe_bulls.pop(inx)

    cow_count = 0
    print(cow_count, masternum, guess, maybe_bulls)






