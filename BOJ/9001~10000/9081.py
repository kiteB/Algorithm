# 단어 맞추기
import sys


def next_permutation(arr):
    i = len(arr) - 2

    # i가 0 이상이고, 뒤에 있는 값이 앞에 있는 값보다 크거나 같으면 계속 탐색
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i == -1:  # 찾지 못하면 False 리턴
        return False

    j = len(arr) - 1  # 뒤에서부터 탐색
    while arr[i] >= arr[j]:  # arr[i]보다 작은 arr[j] 값을 탐색
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]  # 값 바꾸기
    result = arr[:i + 1]  # 처음부터 i까지 result에 넣는다.
    result.extend(list(reversed(arr[i + 1:])))  # i 이후부터는 뒤집어서 result에 넣는다.

    return result


T = int(sys.stdin.readline())
for _ in range(T):
    word = list(sys.stdin.readline().strip())
    answer = next_permutation(word)

    if not answer:  # 답을 찾지 못했으면 주어진 단어 출력
        print(''.join(word))
    else:
        print(''.join(answer))
