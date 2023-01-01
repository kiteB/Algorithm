# iSharp
import sys

case = sys.stdin.readline().replace(',', '').replace(';', '').split()
basic = case[0]

for variable in case[1:]:  # 추가적인 변수형
    alpha = []
    temp = []

    for v in variable:
        if v.isalpha():
            alpha.append(v)
        else:
            if v == '[':
                temp.append(']')
            elif v == ']':
                temp.append('[')
            else:
                temp.append(v)

    print(basic + ''.join(temp[::-1]) + ' ' + ''.join(alpha) + ';')