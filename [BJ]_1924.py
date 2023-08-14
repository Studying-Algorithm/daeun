start = ["MON", "THU", "THU", "SUN", "TUE", "FRI", "SUN", "WED", "SAT", "MON", "THU", "SAT"]
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

month, date = map(int, input().split())
start_day = start[month-1]

check = date % 7  # 날짜(일)을 7로 나눈 나머지 저장
idx = day.index(start_day) # 무슨 요일부터 시작하는지 idx에 그 인덱스 저장

res = (check + idx) % 7 - 1
result = day[res]

print(result)
