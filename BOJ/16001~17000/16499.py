# 동일한 단어 그룹화하기
import sys

n = int(sys.stdin.readline())
words = []

for _ in range(n):
    word = sorted(list(sys.stdin.readline().strip()))

    if word in words:
        continue
    else:
        words.append(word)

print(len(words))