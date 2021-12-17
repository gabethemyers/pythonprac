




def gameboard(size):
    top = ' ---'
    mid = '|   '
    topresult = ''
    midresult = ''
    for i in range(size + 1):
        midresult = midresult + mid
    for i in range(size):
        topresult = topresult + top
    for i in range(size):
        print(topresult)
        print(midresult)
        print(topresult)

gameboard(8)