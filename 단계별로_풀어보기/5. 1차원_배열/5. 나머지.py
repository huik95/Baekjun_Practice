arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))

#arr배열을 만듬
#for문으로 arr배열에 나눈 값을 넣음
#배열을 set으로 중복제거
#len으로 갯수 표현