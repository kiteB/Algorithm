# Project Teams
import sys
input = sys.stdin.readline

n = int(input())
students = list(map(int, input().split()))
students.sort()
answer = []

for i in range(n * 2):
    answer.append(students[i] + students[n * 2 - 1 - i])

print(min(answer))
