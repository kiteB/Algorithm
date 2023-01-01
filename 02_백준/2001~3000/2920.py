# 다장조는 c d e f g a b C, 총 8개음으로 이루어져 있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다.
# c는 1로, d는 2로, ..., C는 8로 바꾼다.
# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘다 아니라면 mixed이다
# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, mixed인지를 판별하는 프로그램을 작성하시오.
import sys

notes = list(map(int, sys.stdin.readline().split()))

if notes == [1, 2, 3, 4, 5, 6, 7, 8]:
    print('ascending')
elif notes == [8, 7, 6, 5, 4, 3, 2, 1]:
    print('descending')
else:
    print('mixed')