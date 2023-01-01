# A와 B
import sys

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())

while len(s) != len(t):

    # 1. S) 문자열의 뒤에 A를 추가한다. -> T) 문자열의 뒤에 A가 있으면 제거한다.
    if t[-1] == 'A':
        t.pop()
    else:   # 2. S) 문자열을 뒤집고 B를 추가한다. -> T) 문자열의 뒤에 B가 있으면 제거하고 뒤집는다.
        t.pop()
        t.reverse()

if s == t:
    print(1)
else:
    print(0)