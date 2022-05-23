for i in range(1, 101):
    count = 0
    for l in range(1, i + 1):
        if (i % l == 0):
            count += 1
    if (count == 2):
        print(i,end=" ")