# 소수 & 팰린드롬
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_palindrome(num):
    return str(num) == str(num)[::-1]


n = int(input())
max_num = 1000000
answer = 0

# 팰린드롬 판별
for i in range(n, max_num + 1):
    if is_palindrome(i) and is_prime(i):
        answer = i
        break

# 범위 내에 답이 없으면
if answer == 0:
    answer = 1003001

print(answer)
