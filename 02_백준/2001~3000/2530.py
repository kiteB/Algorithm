# 인공지능 시계
import sys

h, m, s = map(int, sys.stdin.readline().split())
d = int(sys.stdin.readline())

second = (s + d) % 60
minute = (m + (s + d) // 60) % 60
hour = (h + (m + (s + d) // 60) // 60) % 24

print(hour, minute, second)