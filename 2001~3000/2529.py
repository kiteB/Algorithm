# 두 종류의 부등호 기호 '<'와 '>'가 k개 나열된 순서열 A가 있다.
# 우리는 이 부등호 기호 앞뒤에 서로 다른 한 자릿수 숫자를 넣어서 모든 부등호 관계를 만족시키려고 한다.
# 부등호 기호 앞뒤로 넣을 수 있는 숫자는 0 ~ 9의 정수이며 선택된 숫자는 모두 달라야 한다.
# 제시된 k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서 최댓값과 최솟값을 찾아야 한다.
# 입력: 첫 줄에 부등호 문자의 개수를 나타내는 정수 k가 주어진다.
# 그 다음 줄에는 k개의 부등호 기호가 하나의 공백을 두고 한 줄에 모두 제시된다. k의 범위는 2 <= k <= 9이다.
# 출력이 제시된 부등호 관계를 만족하는 k+1 자리의 최대, 최소 정수를 첫째 줄과 둘째 줄에 각각 출력해야 한다.
# 단 첫 자리가 0인 경우도 정수에 포함되어야 한다. 모든 입력에 답은 항상 존재하며 출력 정수는 하나의 문자열이 되도록 해야 한다.
import sys
from itertools import permutations

k = int(sys.stdin.readline())   # 부등호의 개수
signs = list(map(str, sys.stdin.readline().split()))     # 제시된 부등호 기호 저장
numbers = list(range(0, 10))    # 0부터 9까지의 숫자 리스트 생성
permute = permutations(numbers, k+1)    # numbers의 순열
flag = False    # 계산 결과의 참/거짓 판별
answer = []     # 참인 경우의 순열을 저장할 리스트 생성

for i in permute:   # 생성된 순열을 하나씩 가져오기
    for j in range(k):  # k만큼 반복
        # 부등호 기호가 '>'인 경우
        if signs[j] == '>':
            if int(i[j]) > int(i[j+1]):  # 계산 결과가 참인 경우
                flag = True
            else:                        # 계산 결과가 거짓인 경우
                flag = False
                break
                
        # 부등호 기호가 '<'인 경우
        elif signs[j] == '<':
            if int(i[j]) < int(i[j+1]):  # 계산 결과가 참인 경우
                flag = True
            else:                        # 계산 결과가 거짓인 경우
                flag = False
                break
    
    # flag가 참인 경우, 순열을 str 형태로 answer에 추가
    if flag:
        answer.append(''.join(map(str, i)))

print(max(answer))
print(min(answer))