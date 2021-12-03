"""Write a program that asks the user how many Fibonacci numbers to generate and then generates them. Take this
opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the
sequence to generate """


# function gets input from user
def get_input():
    return int(input('how many fibonacci numbers: '))


# function to return x number of fibonacci number in a list
# I first initialize a list with two 1s because then create a for loop that append the last element in the list plus
# the second to last element in the list
def fibonacci(nums):
    result = [1, 1]
    for i in range(nums):
        result.append(result[-2] + result[-1])
    return result
