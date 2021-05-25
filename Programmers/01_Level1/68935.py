# 3진법 뒤집기
def solution(n):
    result = ''
    answer = 0

    while n != 0:
        result += str(n % 3)
        n //= 3

    for i in range(len(result)):
        answer += pow(3, len(result) - i - 1) * int(result[i])

    return answer