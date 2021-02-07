# 알파벳 대문자로 구성되어있는 문자열 S가 주어졌을 때, S에 등장하지 않는 알파벳 대문자의 아스키 코드 값의 합을 구하는 프로그램을 작성하시오.
# A는 65, Z는 90
# 입력: T개의 테스트 데이터로 구성된다.

import sys

T = int(sys.stdin.readline())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(T):
    sum = 0
    S = sys.stdin.readline()

    for each in alphabet:
        if each not in S:
            sum += int(ord(each))
    print(sum)