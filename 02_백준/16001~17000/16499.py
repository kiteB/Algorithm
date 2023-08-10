# 동일한 단어 그룹화하기
import sys
input = sys.stdin.readline

n = int(input())
words = set()

for _ in range(n):
    word = ''.join(sorted(input().strip()))
    words.add(word)

print(len(words))
