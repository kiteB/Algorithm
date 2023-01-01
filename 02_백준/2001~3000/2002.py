# 추월
import sys

n = int(sys.stdin.readline())
in_cars = dict()
out_cars = []

for i in range(n):
    car = sys.stdin.readline().strip()
    in_cars[car] = i

for _ in range(n):
    car = sys.stdin.readline().strip()
    out_cars.append(car)

overtaking = 0
for i in range(n - 1):
    for j in range(i + 1, n):   # 현재 차 뒤에 있는 차량들과 비교
        if in_cars[out_cars[i]] > in_cars[out_cars[j]]:     # 현재 차량보다 먼저 들어간 차량이 있다면
            overtaking += 1
            break

print(overtaking)