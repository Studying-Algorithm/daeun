# 백준 11653번 - 소인수분해

def Divider(number, i):
    while True:
        if number == 1:
            break
        if number % i == 0:
            number = appendToFactors(number, i)
        else:
            i += 1
    return factors

def appendToFactors(number, i):
    factors.append(i)
    number //= i
    return number


factors = []
number = int(input())
i = 2
factors = Divider(number, i)
for factor in factors:
    print(factor)
