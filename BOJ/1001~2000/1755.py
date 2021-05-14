# 79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다. 80은 마찬가지로 "eight zero"라고 읽는다.
# 79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.
# 문제는 정수 M, N(1 ≤ M, N ≤ 99)이 주어지면 M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.
# 입력: 첫째 줄에 M과 N이 주어진다.
# 출력: M 이상 N 이하의 정수를 문제 조건에 맞게 정렬하여 한 줄에 10개씩 출력한다.
import sys

M, N = map(int, sys.stdin.readline().split())
num_dic = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
           5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

idx = list(range(M, N+1))               # M부터 N 까지의 숫자 저장
numbers = {}

for i in idx:
    i = str(i)
    new = ''
    for num in i:
        new += num_dic[int(num)]
        new += ' '
    numbers[i] = new

idx = 1
for key, val in sorted(numbers.items(), key=lambda x: x[1]):
    if idx % 10 == 0:
        print(key)
    else:
        print(key, end=' ')
    idx += 1