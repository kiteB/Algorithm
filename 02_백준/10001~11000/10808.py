# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
import sys

case = sys.stdin.readline()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    cnt = case.count(i)
    print(cnt, end=' ')