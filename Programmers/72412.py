from itertools import combinations


def solution(info, query):
    answer = []
    applicants = {}         # 지원자의 정보의 모든 조합을 저장할 딕셔너리

    for i in info:
        i = i.split()
        score = int(i[-1])  # 점수 분리
        tmp = i[:-1]        # 점수를 제외한 나머지 정보 저장

        # 모든 조합을 구해서 저장하기
        for j in range(5):
            for c in combinations(tmp, j):
                tmp2 = ''.join(c)

                if tmp2 in applicants:
                    applicants[tmp2].append(score)
                else:
                    applicants[tmp2] = [score]

    # 점수를 기준으로 오름차순으로 지원자 정보 정렬
    for key in applicants.keys():
        applicants[key].sort()

    # 쿼리 가공
    for q in query:
        q = q.split()
        q_score = int(q[-1])
        q_infos = q[:-1]

        while 'and' in q_infos:
            q_infos.remove('and')

        while '-' in q_infos:
            q_infos.remove('-')

        q = ''.join(q_infos)
        # print(q)
        cnt = 0
        if q in applicants.keys():
            for i in applicants[q]:
                if i >= q_score:
                    cnt += 1

        answer.append(cnt)
    return answer

