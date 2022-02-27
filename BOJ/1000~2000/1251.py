# 단어 나누기
import sys

word = list(sys.stdin.readline().strip())
answer = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a = word[:i][::-1]
        b = word[i:j][::-1]
        c = word[j:][::-1]
        answer.append(''.join(a + b + c))

print(sorted(answer)[0])
