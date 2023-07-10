# 피보나치 수 5 - 브론즈 2
n = int(input())
fibo = [0, 1, 1] + [0] * (n - 2)
for i in range(2, n + 1):
    fibo[i] = fibo[i - 2] + fibo[i - 1]

print(fibo[n])
