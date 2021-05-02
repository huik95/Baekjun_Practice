a = int(input())
b = list(map(int, input().split()))
print(f'{min(b)} {max(b)}')

#여러 숫자를 담을 수 있는 map함수와 간격마다 끊는 split함수를 이용
#min, max 함수 사용