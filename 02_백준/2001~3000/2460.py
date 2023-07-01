# 지능형 기차 2 - 브론즈 3
answer = [0] * 10
tmp = 0

for i in range(10):
    a, b = map(int, input().split())
    tmp -= a
    tmp += b
    answer[i] = tmp

print(max(answer))
