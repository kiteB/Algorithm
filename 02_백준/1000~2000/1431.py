# 시리얼 번호
import sys
input = sys.stdin.readline


def sum_num(s):
    return sum(int(char) for char in s if char.isdigit())


n = int(input())
guitars = [input().strip() for _ in range(n)]
guitars.sort(key=lambda x: (len(x), sum_num(x), x))
print(*guitars, sep='\n')
