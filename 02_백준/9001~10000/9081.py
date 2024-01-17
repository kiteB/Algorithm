# 단어 맞추기
import sys
input = sys.stdin.readline


def find_next_permutation(arr):
    i = len(arr) - 2

    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i == -1:
        return ''.join(arr)

    j = len(arr) - 1
    while arr[i] >= arr[j]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return ''.join(arr)


T = int(input())
for _ in range(T):
    word = list(input().strip())
    answer = find_next_permutation(word)
    print(answer)
