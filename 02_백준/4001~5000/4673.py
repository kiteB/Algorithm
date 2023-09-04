# 셀프 넘버
def solve(num):
    result = num

    while num != 0:
        result += num % 10
        num //= 10

    return result


numbers = []
for i in range(1, 10001):
    numbers.append(solve(i))

    if i not in numbers:
        print(i)
