def solution(s):
    # 문자열의 길이가 1인 경우는 압축할 수 없으므로 그대로 1 리턴
    if len(s) == 1:
        return 1

    answer = []

    # 1부터 len(s)//2 까지 문자열을 잘라보기
    for unit in range(1, len(s) // 2 + 1):
        result = ''
        cnt = 1

        # unit만큼 문자열을 잘라보면서 비교해보기
        for i in range(0, len(s), unit):
            tmp = s[i: (i+unit)]                # 기준 문자열
            new = s[(i+unit):(i+2*unit)]        # 새로운 문자열

            # 문자열 압축이 가능한 경우
            if tmp == new:
                cnt += 1
            else:
                if cnt > 1:
                    result += str(cnt) + tmp
                else:
                    result += tmp
                cnt = 1

        answer.append(len(result))
    return min(answer)
