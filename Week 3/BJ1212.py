import sys

def octalToDecimal(o):
    b = []
    for _ in range(3): # 2진수 만들기 
        b.append(o % 2)
        o //= 2
    b.reverse()
    return b
    

octal = sys.stdin.readline().rstrip()
res = []

for o in octal: # "314"에서 '3', '1', '4'가 o
    binary = octalToDecimal(int(o))
    res.append(binary)
    for _ in range(2): # 맨 앞은 1로 시작
        if res[0][0] == 0:
            del res[0][0]

    
result = sum(res, [])
for r in result:
    print(r, end='')
