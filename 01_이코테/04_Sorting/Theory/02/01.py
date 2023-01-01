import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    name, score = sys.stdin.readline().split()
    data.append([name, int(score)])

data = sorted(data, key=lambda x: x[1])
for item in data:
    print(item[0], end=' ')