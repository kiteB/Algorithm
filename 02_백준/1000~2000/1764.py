# 듣보잡
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
not_heard = set([input().rstrip() for _ in range(n)])
never_seen = set([input().rstrip() for _ in range(m)])
result = sorted(list(not_heard & never_seen))   # 교집합 구하기

print(len(result))
print(*result, sep='\n')
