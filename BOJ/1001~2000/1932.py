# 주어진 크기가 5인 정수 삼각형의 그림을 참고하라.
# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
# 삼각형의 크기는 1 이상 500 이하이며, 삼각형을 이루고 있는 각 수는 모두 정수이다.
# 입력: 첫째 줄에 삼각형의 크기 n이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.
# 출력: 첫째 줄에 최대가 되는 경로에 있는 수의 합을 출력한다.
import sys

n = int(sys.stdin.readline())
triangle = []

for i in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(i+1):
        # 맨 왼쪽의 경우
        if j == 0:
            triangle[i][0] = triangle[i-1][0] + triangle[i][0]
        # 맨 오른쪽의 경우
        elif i == j:
            triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
        # 가운데일 경우
        else:
            triangle[i][j] = max(triangle[i-1][j-1] + triangle[i][j], triangle[i-1][j] + triangle[i][j])

print(max(triangle[n-1]))