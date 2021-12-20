# 한국이 그리울 땐 서버에 접속하지
import sys

n = int(sys.stdin.readline())
pattern = sys.stdin.readline().strip()
pre, post = pattern.split('*')

for _ in range(n):
    case = sys.stdin.readline().rstrip()

    start = case.find(pre)
    substring = case[len(pre):][::-1]
    end = substring.find(post[::-1])

    if start == 0 and end == 0:
        print('DA')
    else:
        print('NE')