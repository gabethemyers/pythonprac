def get_input():
    return(int(input('how many fibinocci numbers: ')))

def fibonaci(nums):
    list = [1, 1]
    for i in range(nums):
        list.append(list[-2] + list[-1])
    return list


input = get_input()

print(fibonaci(input))