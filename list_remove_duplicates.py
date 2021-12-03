# function to remove duplicate elements in a list using lists
def remove_dup_list(x):
    result = []
    # loop that goes through each item in the input list and as long as
    # that item is not already in the result it appends it
    for item in x:
        if item not in result:
            result.append(item)
    return result


# function that uses sets to remove duplicate items
def remove_dup_set(x):
    # since sets cant have duplicates I just turn it into a set then back to a list
    return list(set(x))


# function that uses a generator to do this even tho problem asks for a list as a result but generators are fun
def remove_dup_gen(x):
    result = []
    # loop that goes through each item in the input list and as long as
    # that item is not already in the result it yields it
    for item in x:
        if item not in result:
            yield item

            #added this for testing ign