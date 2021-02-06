# 설문조사 결과를 통해 준희가 귀여운지 아닌지 알아보자.
# N개의 줄에는 각 줄마다 각 사람이 설문 조사에 어떤 의견을 표명했는지를 나타내는 정수가 주어진다.
# 0은 준희가 귀엽지 않다는 뜻이고, 1은 준희가 귀엽다는 뜻이다.
# 준희가 귀엽지 않다는 의견이 더 많을 경우 "Junhee is not cute!"를 출력하고, 귀엽다는 의견이 더 많을 경우 "Junhee is cute!"를 출력하라.
import sys

N = int(sys.stdin.readline())
ans = 0

for _ in range(N):
    opinion = int(sys.stdin.readline())

    if opinion == 1:
        ans += 1
    else:
        ans -= 1

if ans >= 1:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")