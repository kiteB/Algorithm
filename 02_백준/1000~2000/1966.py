# 프린터 큐
import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    docs = deque(map(int, sys.stdin.readline().split()))
    cnt = 0     # 출력한 문서의 개수

    while True:
        max_val = max(docs)     # 가장 높은 중요도
        front = docs.popleft()  # docs의 front 빼기
        m -= 1  # m을 조정하여 docs[m]에 해당하는 문서의 위치를 기억한다.

        if front == max_val:    # 첫 번째 요소가 최댓값이라면
            cnt += 1

            if m == -1:     # 첫 번째 요소가 우리가 찾고자 하는 문서였다면
                print(cnt)
                break

        else:   # 최댓값이 아니라면 뒤에 삽입
            docs.append(front)

            if m < 0:   # 문서의 마지막을 가리키도록 조정
                m = len(docs) - 1
