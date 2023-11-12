# 1로 만들기 2
n = int(input())

dp = [i for i in range(n + 1)]
dp[1] = 0
answer = [i for i in range(n + 1)]
answer[1] = 0

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    answer[i] = i - 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        answer[i] = i // 3

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        answer[i] = i // 2

print(dp[n])
print(n, end=' ')

target = n
while answer[target] != 0:
    print(answer[target], end=' ')
    target = answer[target]