# Hashing
import sys

l = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

answer = 0
for i in range(l):
    answer += (ord(s[i]) - 96) * pow(31, i)

print(answer % 1234567891)