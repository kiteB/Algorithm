# 문자열 집합 - dict 이용 (116 ms)
# 딕셔너리의 키는 해시 함수를 통해 해시값으로 매핑된다.
# 주어진 단어를 검색할 때 해시 테이블을 이용하기 때문에 빠른 검색이 가능하다.
# 시간 복잡도: O(m + n)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = dict()

for _ in range(n):
    word = input().rstrip()
    s[word] = True

answer = 0
for _ in range(m):
    word = input().rstrip()

    if word in s.keys():
        answer += 1

print(answer)
