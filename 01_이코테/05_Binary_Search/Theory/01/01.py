import sys

n = int(sys.stdin.readline())
store = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
customer = list(map(int, sys.stdin.readline().split()))

# 가게의 부품들을 오름차순으로 정렬
store.sort()


def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 원하는 값을 찾은 경우
        if store[mid] == target:
            return True
        # 원하는 값보다 큰 경우
        elif store[mid] > target:
            end = mid - 1
        # 원하는 값보다 작은 경우
        else:
            start = mid + 1
    return False


for i in customer:
    answer = binary_search(i, 0, n-1)

    if answer:
        print('yes', end=' ')
    else:
        print('no', end=' ')