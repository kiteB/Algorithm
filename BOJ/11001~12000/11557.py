# Yangjojang of The Year
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    school = [list(sys.stdin.readline().split()) for _ in range(n)]
    school.sort(key=lambda x: -int(x[1]))
    print(school[0][0])