# 숫자 문자열과 영단어
def solution(s):
    numbers = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
               'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    tmp = ''
    answer = ''

    for i in s:
        # 숫자면 answer에 바로 더하기
        if i.isdigit():
            answer += i
        else:
            tmp += i
            if tmp in numbers.keys():
                answer += numbers[tmp]
                tmp = ''

    return int(answer)