S = int(input())

toS = 0
cnt = 0
for i in range(1, S+1):
    toS += i
    left = S - toS   # S까지 남은 숫자 확인
    if left < 0:
        break
    else:
        cnt += 1
        
print(cnt)