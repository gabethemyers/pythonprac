# opens file and puts all text to one variable
with open('SUN_Data.txt', 'r') as open_file:
    all_text = open_file.read()

# didnt want to teal with .readline() so now i am massaging data
all_text = all_text.split('\n')

# splitting the url then grabbing the 2 element
catagories = []
for line in all_text:
    catagories.append(line.split('/')[2])

# initializing all catagories
diction = {}
for catagory in catagories:
    diction[catagory] = 0

# idk why I have to do this but I cant just += a dict value so I gotta do this
for catagory in catagories:
    temp = diction[catagory]
    temp += 1
    diction[catagory] = temp

print(diction)
