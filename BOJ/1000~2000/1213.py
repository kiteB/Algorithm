# 팰린드롬 만들기
import sys

name = sys.stdin.readline().strip()
alphabet = [0] * 26

for i in name:
    alphabet[ord(i) - 65] += 1

odd = ''
odd_cnt = 0
answer = ''
for idx, val in enumerate(alphabet):
    if val % 2 == 1:
        odd_cnt += 1  # 알파벳 등장 횟수가 홀수 개인 경우
        odd = chr(idx + 65)
    answer += chr(idx + 65) * (alphabet[idx] // 2)

if odd_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(answer + odd + answer[::-1])
