"""Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password. Include your run-time code in a main method. """

from random import choice


# this function explains to the user how the program works and asks for what characters they want and how long it should
# be, then returns them
def inputs():
    char_choice = input('\nFor each group of characters that you want in your password type the number that '
                        'corresponds to it:\n 1: uppercase letters\n 2: lowercase letters\n 3: numbers\n 4: special '
                        'characters \nfor example if you only want uppercase letters and numbers type:13\n \nType '
                        'here: ')
    length = int(input('How long would you like your password to be? '))
    return char_choice, length


def main():
    # here i initialize and create all variables that I will need
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    special_chars = "!@#$%^&*=+?"
    user_input = inputs()
    char_choice = user_input[0]
    length = user_input[1]
    chars_to_choose_from = ''
    result = ''

    # Here I am seeing what the user wants in their password and then adding that character group to a final string that
    # i will choose from
    if '1' in char_choice:
        chars_to_choose_from += capital_letters
    if '2' in char_choice:
        chars_to_choose_from += lowercase
    if '3' in char_choice:
        chars_to_choose_from += numbers
    if '4' in char_choice:
        chars_to_choose_from += special_chars

    # this is just a loop that randomly chooses and adds that character to the final password, it is choosing from the
    # string I created above using the users choices.
    for i in range(length):
        result += choice(chars_to_choose_from)
    return f'Your {length} character password is: {result}'


if __name__ == '__main__':
    print(main())
