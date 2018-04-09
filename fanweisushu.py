list = []
i = 2
for i in range(2, 10000000):
    j = 2
    for j in range(2, int(i**0.5)+1):
        if(i % j == 0):
            break
    else:
        list.append(i)
print(list)
