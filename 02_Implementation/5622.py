# 알파벳 대문자로 이루어진 단어가 주어질 때, 다이얼을 걸기 위해 필요한 최소 시간 출력
case = input()
count = 0

for i in case:
    if i == 'A' or i == 'B' or i == 'C':
        count += 3
    elif i == 'D' or i == 'E' or i == 'F':
        count += 4
    elif i == 'G' or i == 'H' or i == 'I':
        count += 5
    elif i == 'J' or i == 'K' or i == 'L':
        count += 6
    elif i == 'M' or i == 'N' or i == 'O':
        count += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        count += 8
    elif i == 'T' or i == 'U' or i == 'V':
        count += 9
    else:
        count += 10

print(count)