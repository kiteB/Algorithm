# 안테나
import sys

n = int(sys.stdin.readline())
house = list(map(int, sys.stdin.readline().split()))
house.sort()

print(house[(n-1)//2])