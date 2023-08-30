def lcm(a, b):
    result = []
    for i in range(1, a * b + 1):
        mul_a = a * i
        mul_b = b * i
        if mul_a == mul_b:
            result.append(mul_a)
    return min(result)

testCase = int(input())

for t in range(testCase):
    a, b = map(int, input().split())
    print(lcm(a, b))
    
