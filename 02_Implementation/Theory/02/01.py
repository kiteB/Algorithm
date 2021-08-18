# 시각
import sys

N = int(sys.stdin.readline())
cnt = 0

# 모든 경우의 수를 따져본다
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(s) or '3' in str(m) or '3' in str(h):
                cnt += 1

print(cnt)