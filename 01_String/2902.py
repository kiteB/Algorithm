# 사람들은 사람 성이 들어간 알고리즘을 두 가지 형태로 부른다.
# 첫 번째는 성을 모두 쓰고, 이를 하이픈(-)으로 이어 붙인 것이다. 이것을 긴 형태로 만든다
# 두 번째로 짧은 형태는 만든 사람의 성의 첫 글자만 따서 부르는 것이다.
# 긴 형태의 알고리즘 이름이 주어졌을 때, 이를 짧은 형태로 바꾸어 출력하는 프로그램을 작성하시오.
import sys

case = sys.stdin.readline().strip().split('-')
ans = []

for i in case:
    ans.append(i[0])
print(''.join(ans))