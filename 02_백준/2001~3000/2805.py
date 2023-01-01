# 상근이는 나무 M 미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다.
# 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할 것이다.
# 목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다.
# 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다.
# 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다.
# 상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다.
# 이때, 적어도 M 미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다.
# 둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다.
# 출력: 적어도 M 미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
import sys


def tree_cutting(target, data):
    start = 0
    end = max(data)

    while start <= end:
        mid = (start + end) // 2
        trees = 0  # 잘린 나무의 합

        for i in data:
            if i > mid:
                trees += i - mid
        
        # 나무의 양이 부족한 경우
        if trees < target:
            end = mid - 1

        # 나무의 양이 충분한 경우
        else:
            result = mid    # 절단기 높이
            start = mid + 1

    return result


N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
print(tree_cutting(M, tree))