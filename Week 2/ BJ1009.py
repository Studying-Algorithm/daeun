import sys

testCase = int(sys.stdin.readline())
for t in range(testCase):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10 # a의 값을 0에서 9사이의 값으로 저장 
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        if b % 2 == 0:
            print(a**2 % 10)
        else:
            print(a)
    elif a == 2 or a == 3 or a == 7 or a == 8:
        b %= 4
        if b == 0:
            print((a**4) % 10)
        else:
            print((a**b) % 10)