# UCPC는 무엇의 약자일까?
import sys

string = str(sys.stdin.readline().strip())
words = ['U', 'C', 'P', 'C']
is_available = True     # UCPC를 만들 수 있는지 여부를 저장할 변수

for i in range(4):
    idx = string.find(words[i])

    if idx != -1:
        string = string[idx+1:]
    else:
        is_available = False
        break

if is_available:
    print('I love UCPC')
else:
    print('I hate UCPC')