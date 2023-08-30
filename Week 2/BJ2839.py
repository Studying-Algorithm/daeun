sugar = int(input())
bags = []
cnt = 0
bag = 0
s = sugar // 3

while sugar > 2:
    if sugar % 5 == 0:
        bag = sugar // 5
        bags.append(bag)
        break
    else:
        if sugar % 3 == 0:
            bag = sugar // 3
            bags.append(bag)
        for i in range(s):
            sugar -= 3
            cnt += 1
            if sugar % 3 == 0:
                bag = sugar // 3 + cnt
                bags.append(bag)
            if sugar % 5 == 0:
                bag = sugar // 5 + cnt
                bags.append(bag)
    
if bags:
    print(min(bags))  # 봉지의 최소 개수 출력 
else: 
    print(-1)