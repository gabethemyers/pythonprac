""" prompt: Write a program (using functions!) that asks the user for a long string containing multiple words. Print
back to the user the same string, except with the words in backwards order. """


# this function splits the string by spaces, then reverses the list, then joins the list with spaces
def reverse_word(string):
    result = string.split(' ')
    result = result[::-1]
    result = ' '.join(result)
    return result




