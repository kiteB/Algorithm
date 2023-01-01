# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
# 입력: 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
# 출력: 직사각형의 네 번째 점의 좌표를 출력한다.
list_x = []
list_y = []

for i in range(3):
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)

for i in range(3):
    if list_x.count(list_x[i]) == 1:
        x = list_x[i]
    if list_y.count(list_y[i]) == 1:
        y = list_y[i]
print(x, y)