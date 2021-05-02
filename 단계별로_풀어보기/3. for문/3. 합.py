def sum1():
    n = int(input())
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
print(sum1()) 

#or

def sum2():
    n = int(input())
    print(n*(n+1)//2)
#sum = (n*(n+1))//2 공식 외워두면 편함.
