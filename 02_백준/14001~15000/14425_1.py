# 문자열 집합 - list 이용 (3748 ms)
# 리스트 내의 모든 원소를 순회하면서 단어를 찾아야 하므로 단어 수가 많아질수록 검색 속도가 증가한다.
# 시간 복잡도: O(m * n)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [input().rstrip() for _ in range(n)]
answer = 0

for _ in range(m):
    word = input().rstrip()

    if word in s:
        answer += 1

print(answer)
