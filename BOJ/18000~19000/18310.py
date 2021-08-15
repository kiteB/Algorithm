# 안테나
import sys

n = int(sys.stdin.readline())
Antenna = list(map(int, sys.stdin.readline().split()))
Antenna.sort()
print(Antenna[(n-1)//2])