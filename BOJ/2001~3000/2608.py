# 로마 숫자
import sys

dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
dict2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}


def to_digit(s):   # 아라비아 숫자로 변환
    idx = 0
    num = 0

    while idx < len(s):
        if idx == len(s) - 1:   # 마지막 인덱스인 경우
            num += dict1[s[idx]]
            break

        if s[idx:idx+2] in dict2:   # 작은 숫자가 큰 숫자의 왼쪽에 오는 경우
            num += dict2[s[idx:idx+2]]
            idx += 2
        else:
            num += dict1[s[idx]]
            idx += 1

    return num


def to_rome(n):  # 로마 숫자로 변환
    rome = ''
    num = str(n)

    place = len(num)
    i = 0

    while i < len(num):     # 각 자릿수마다 특이 케이스를 조건문으로 나눠서 바꿔준다.
        if place == 4:
            rome += 'M' * int(num[i])
        elif place == 3:
            if int(num[i]) == 4:
                rome += 'CD'
            elif int(num[i]) == 9:
                rome += 'CM'
            else:
                if int(num[i]) >= 5:
                    rome += 'D'
                rome += 'C' * (int(num[i]) % 5)
        elif place == 2:
            if int(num[i]) == 4:
                rome += 'XL'
            elif int(num[i]) == 9:
                rome += 'XC'
            else:
                if int(num[i]) >= 5:
                    rome += 'L'
                rome += 'X' * (int(num[i]) % 5)
        else:
            if int(num[i]) == 4:
                rome += 'IV'
            elif int(num[i]) == 9:
                rome += 'IX'
            else:
                if int(num[i]) >= 5:
                    rome += 'V'
                rome += 'I' * (int(num[i]) % 5)
        i += 1
        place -= 1

    return rome


num1 = sys.stdin.readline().strip()
num2 = sys.stdin.readline().strip()

digit = to_digit(num1) + to_digit(num2)
print(digit)
print(to_rome(digit))
