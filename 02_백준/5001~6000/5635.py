# 생일
import sys

n = int(sys.stdin.readline())
students = [sys.stdin.readline().split() for _ in range(n)]
students.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(students[n - 1][0])   # 나이가 가장 적은 사람
print(students[0][0])       # 나이가 가장 많은 사람