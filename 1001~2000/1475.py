# 다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.
# 다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0 ~ 9번까지 숫자가 하나씩 들어있다.
# 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6번과 9번은 서로 뒤집어서 사용할 수 있다)
# 입력: 첫째 줄에 다솜이의 방 번호 N이 주어진다.
# 출력: 첫째 줄에 필요한 세트의 개수를 출력한다.
import sys
import math

N = list(map(int, sys.stdin.readline().strip()))
numbers = [0] * 10

for i in N:
    if i == 6 or i == 9:
        numbers[5] += 0.5
    else:
        numbers[i] += 1

print(math.ceil(max(numbers)))