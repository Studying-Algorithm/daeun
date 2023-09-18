# 백준 1978번 - 소수찾기

def primeDiscriminator(num):
    result = 1 
    if num == 1:
        result = 0
    for i in range(2, num):
        if num % i == 0:
            result = 0
    return result

n = input()
check_prime = list(map(int, input().split()))

prime_count = 0
for num in check_prime:
    prime_count += primeDiscriminator(num)
    
print(prime_count)
 