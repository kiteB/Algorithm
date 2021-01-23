# 캠핑장은 연속하는 20일 중 10일 동안만 사용할 수 있다.
# 등산가 김강산이 가족과 함께 28일에 캠핑 휴가를 시작했을 때, 휴가 기간동안 캠핑장을 며칠동안 사용할 수 있을까?
# 더 일반화하여 캠핑장을 연속하는 P일 중, L일 동안만 사용할 수 있다고 할 때, 강산이는 이제 막 V일짜리 휴가를 시작했다. 강산이사 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)
# 입력: 각 테스트 케이스는 L, P, V를 순서대로 포함하고 있다. 모든 입력 정수는 int 범위이며, 마지막 줄에는 0이 3개 주어진다.
# 출력: Ex) Case 1: 14 (테스트 케이스 순서와 최대 일수를 출력하라)
import sys

idx = 1
while True:
    L, P, V = map(int, sys.stdin.readline().split())
    cnt = 0
    # 0 0 0 이 입력되었을 때 종료
    if L*P*V == 0:
        break

    else:
        cnt += (V // P) * L

        if V % P <= L:
            cnt += V % P
        else:
            cnt += L

        print('Case {}: {}'.format(idx, cnt))
        idx += 1
