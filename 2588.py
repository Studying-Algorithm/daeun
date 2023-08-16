num1 = int(input())
num2 = int(input())

num2_1 = num2 % 10 # 일의 자리 수
num2_10 = num2 // 10 % 10 # 십의 자리 수
num2_100 = num2 // 100 # 백의 자리 수

res1 = num1 * num2_1
res2 = num1 * num2_10  
res3 = num1 * num2_100 
# 더해지는 자릿수를 맞추기 위해 10, 100 곱해서 더함
num_sum = res1 + (res2 * 10) + (res3 * 100)
print(res1)
print(res2)
print(res3)
print(num_sum)
