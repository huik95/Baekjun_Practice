n = int(input())
for _ in range(n):
    a = list(input())
    sum = 0
    b = 1
    for i in a:
        if i == 'O':
            sum += b
            b += 1
        else:
            b = 1
    print(sum)