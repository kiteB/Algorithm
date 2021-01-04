# 알파벳 소문자로만 이루어진 단어 S가 주어질 때 각각의 알파벳에 대해서,
# 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않는 경우에는 -1을 출력하는 프로그램 작성하기
from string import ascii_lowercase

case = input()
alphabet = list(ascii_lowercase)

for i in alphabet:
    print(case.find(i), end=' ')    # find 함수는 특정문자가 처음 등장하는 위치를 출력
