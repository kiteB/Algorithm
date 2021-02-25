# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N이 주어진다.
# 둘째 줄에는 숫자 카드가 적혀있는 정수가 주어진다. 셋째 줄에는 M이 주어진다.
# 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다.
import sys
from bisect import bisect_left, bisect_right


def binary_search(target, data):
    left = bisect_left(data, target)
    right = bisect_right(data, target)
    return right - left


N = int(sys.stdin.readline())
N_cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_cards = list(map(int, sys.stdin.readline().split()))
N_cards.sort()

for i in range(M):
    print(binary_search(M_cards[i], N_cards), end=' ')
