# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타내는 경우만을 말함.
# Ex) 그룹 단어인 경우: ccazzzzbb
# Ex) 그룹 단어가 아닌 경우: aabbbccb
# 첫째 줄에는 단어의 개수 N이 출력됨.
N = int(input())    # 단어의 개수
count = 0           # 그룹 단어의 개수

for i in range(N):
    case = input()
    words = []

    for j in range(len(case)):
        if case[j] not in words:
            words.append(case[j])

        elif (case[j] in words) and (case[j-1] == case[j]):
            words.append('.')

        elif (case[j] in words) and (case[j-1] != case[j]):
            break

    if len(words) == len(case):
         count += 1

print(count)