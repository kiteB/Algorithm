# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 즐부터 보도 못한 사람의 이름이 순서대로 주어진다.
# 이름은 띄어쓰기 없이 영어 소문자로만 이루어지며, 그 길이는 20이하이다.
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
# 출력: 듣보잡의 수와 그 명단을 사전순으로 출력한다.
import sys

N, M = map(int, sys.stdin.readline().split())
not_heard = set()
never_seen = set()

for _ in range(N):
    not_heard.add(sys.stdin.readline().strip())

for _ in range(M):
    never_seen.add(sys.stdin.readline().strip())

result = sorted(list(not_heard & never_seen))

print(len(result))
for i in result:
    print(i)