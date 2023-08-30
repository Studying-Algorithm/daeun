def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    
testCase = int(input())

for t in range(testCase):
    a, b = map(int, input().split())
    lcm = a * b // gcd(a, b)
    print(lcm)
    

    
