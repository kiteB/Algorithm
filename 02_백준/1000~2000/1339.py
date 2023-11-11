# 단어 수학
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

word_dict = defaultdict(int)
for i in range(n):
    for j, val in enumerate(words[i]):
        word_dict[val] += pow(10, len(words[i]) - j - 1)

result = sorted(word_dict.items(), key=lambda x: -x[1])
answer = 0
num = 9
for key, val in result:
    answer += num * val
    num -= 1

print(answer)
