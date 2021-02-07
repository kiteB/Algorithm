# 진영 주식회사가 신규 사원 채용을 실시한다. 인재 선발 시험은 1차 서류심사와 2차 면접 시험으로 이루어진다.
# 진영 주식회사는 다른 모든 지원자와 비교했을 때, 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다.
# 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
# 이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원 수를 구하는 프로그램을 작성하시오.
import sys

T = int(sys.stdin.readline())   # 각 테스트 케이스의 개수

for i in range(T):
    N = int(sys.stdin.readline())     # 각 지원자의 수
    scores = []
    cnt = 0
    scores_1 = set()
    scores_2 = set()

    for j in range(N):
        scores.append(list(map(int, sys.stdin.readline().split())))
    scores = sorted(scores, key=lambda x: (x[0], x[1]))

    scores_1.add(scores[0][0])
    scores_2.add(scores[0][1])
    cnt += 1

    for j in range(1, N):
        if scores[j][0] <= min(scores_1) or scores[j][1] <= min(scores_2):
            scores_1.add(scores[j][0])
            scores_2.add(scores[j][1])
            cnt += 1

    print(cnt)