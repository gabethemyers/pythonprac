"""prompt: randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user
guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong
place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user
guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game
and tell the user at the end. """


import random


def user_input():
    guess = str(input('Enter your guess: '))
    return guess


def find_bulls(guess, masternum):
    count = 0
    list_masternum = list(masternum)
    list_guess = list(guess)
    clist_guess = list_guess.copy()
    for inx, ele in enumerate(list_masternum):
        if list_masternum[inx] == list_guess[inx]:
            clist_guess.remove(ele)
    for ele in clist_guess:
        if ele in list_masternum:
            list_masternum.remove(ele)
            count += 1
    return count


def find_cows(guess, masternum):
    count = 0
    list_masternum = list(masternum)
    list_guess = list(guess)
    for inx, ele in enumerate(list_masternum):
        if list_masternum[inx] == list_guess[inx]:
            count += 1
    return count


masternum = ''
guess = ''
guess_count = 0
for i in range(4):
    masternum = masternum + str((random.randrange(0, 10)))


while guess != masternum:
    guess = user_input()
    if len(guess) > 4 or len(guess) < 4:
        print('Guess must be 4 numbers long')
        continue

    cow_count = find_cows(guess, masternum)
    bull_count = find_bulls(guess, masternum)

    print(f'{bull_count} bulls, {cow_count} cows')
    guess_count += 1

    if guess == masternum:
        break

print(f'You won!, the number was {masternum}')



