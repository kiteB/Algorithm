# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로
# 입력: 첫째 줄에 단어의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
# 출력: 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
import sys

N = int(sys.stdin.readline())
words = []

for i in range(N):
    words.append(sys.stdin.readline().strip())

ans = list(set(words))
ans.sort(key=lambda x: (len(x), x))

for i in ans:
    print(i)

