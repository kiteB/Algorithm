# solved.ac
import sys
input = sys.stdin.readline


def round_func(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


n = int(input())

if n == 0:
    print(0)
else:
    opinions = [int(input()) for _ in range(n)]
    opinions.sort()

    exclude_cnt = round_func(n * 0.15)
    trimmed_data = opinions[exclude_cnt:-exclude_cnt] if exclude_cnt > 0 else opinions
    print(round_func(sum(trimmed_data) / len(trimmed_data)))
