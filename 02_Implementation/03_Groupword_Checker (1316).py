# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타내는 경우만을 말함.
# Ex) 그룹 단어인 경우: ccazzzzbb
# Ex) 그룹 단어가 아닌 경우: aabbbccb
# 첫째 줄에는 단어의 개수 N이 출력됨.
N = int(input())    # 단어의 개수
count = 0           # 그룹 단어의 개수

for i in range(N):
    case = input()
    words = []      # case에 나온 단어를 저장하기 위한 리스트

    for j in range(len(case)):
        if case[j] not in words:    # case의 단어가 words에 없다면,
            words.append(case[j])   # words에 단어 추가

        elif (case[j] in words) and (case[j-1] == case[j]): # case의 단어가 words에 있고, 바로 전에 나온 단어와 동일하다면
            words.append('.')       # words에 '.' 추가

        elif (case[j] in words) and (case[j-1] != case[j]): # case의 단어가 words에 있고, 바로 전에 나온 단어와 다르다면 그룹 단어의 조건 충족 X
            break                                           # for문을 빠져나감.

    if len(words) == len(case):
         count += 1

print(count)