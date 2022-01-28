"""
this program returns user chosen amount of random words from the word list.
"""
import random


def main():
    # opening file and then putting each word as an element in a list
    with open("word_list.txt", "r") as file:
        lines = file.readlines()
        word_list = [line.rstrip() for line in lines]

    user_in = int(input("How many words would you like: "))
    length = len(word_list)

    # gets random word from wordlist x amount of times, determined by user
    result = [word_list[random.randint(0, length)] for i in range(user_in)]

    final = " ".join(result)
    print(final)


if __name__ == "__main__":
    main()
