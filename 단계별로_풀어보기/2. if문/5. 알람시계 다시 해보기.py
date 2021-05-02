h, m = map(int, input().split())

time = h*60+m-45
if time<0:          #만약 시간이 0시 이전으로 바뀐다면, 24시로 변경해주어야 하기 때문에,
    time += 1440    #24시간을 더해준다.
print(time//60, time%60)
