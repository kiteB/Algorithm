# 저작권
import sys

count, avg = map(int, sys.stdin.readline().split())
print(count * (avg - 1) + 1)
