# 실패율 - 10분
def solution(N, stages):
    rates = {}              # 실패율 저장할 딕셔너리
    total = len(stages)     # 스테이지에 멈춰있는 플레이어 수

    for i in range(1, N + 1):           # 1부터 N까지
        if total > 0:
            cnt = stages.count(i)       # 스테이지 번호 등장 횟수
            rates[i] = cnt / total      # 실패율 계산
            total -= cnt
        else:
            rates[i] = 0

    # 실패율(value)을 기준으로 내림차순으로 정렬한 값 return
    return sorted(rates, key=lambda x: -rates[x])


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])