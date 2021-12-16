nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist = []
# I want n for each n in nums using for loop
for n in nums:
    mylist.append(n)

# I want n for each n in nums using list comp
mylist = [n for n in nums]

# i want n*n for each n in nums
mylist = [n*n for n in nums]

# i want n for each n in nums if n is even
mylist = [n for n in nums if n % 2 == 0]

# i want a (letter, num) pair for each letter in 'abcd' and each num in '0123'
mylist = [(letter, num) for letter in 'abcd' for num in range(4)]


# Dictionary comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# i want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
my_dict = {name: hero for name, hero in zip(names,heros)}

# Set comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
myset = {n for n in nums}

# Generator expressions
numd = [1, 2, 3, 4, 5, 6, 7, 8, 9[]
# normal
def genfunc(nums):
    for n in nums:
        yield n*n
my_gen = genfunc(nums)
for i in my_gen:
    print(i)

# expressin


