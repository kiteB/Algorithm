from itertools import combinations


def solution(orders, course):
    answer = []

    for i in course:
        menus = {}              # 메뉴의 조합과 등장 횟수를 저장할 딕셔너리

        for order in orders:
            for c in list(combinations(sorted(order), i)):
                if c in menus:      # 기존 menus에 있는 조합이라면 +1
                    menus[c] += 1
                else:               # 없는 조합이라면 1
                    menus[c] = 1

        menus = sorted(menus.items(), key=lambda x: -x[1])      # 많이 등장한 순서대로 정렬해주기

        for idx in range(len(menus)):
            if menus[idx][1] == menus[0][1] and menus[idx][1] >= 2:
                answer.append(''.join(menus[idx][0]))

    return sorted(answer)