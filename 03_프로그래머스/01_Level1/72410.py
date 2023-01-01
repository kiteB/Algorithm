# 신규 아이디 추천
def solution(new_id):
    answer = ''

    # 1단계 모든 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2단계 알파벳 소문자, 숫자, 빼기, 밑즐, 마침표 제외한 모든 문자 제거
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            answer += i

    # 3단계 마침표 2번 이상 연속되면 하나의 마침표로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계 마침표가 처음이나 끝에 위치하면 제거 (빈 문자열이면 안됨)
    if answer:
        if answer[0] == '.':
            answer = answer[1:]

    if answer:
        if answer[-1] == '.':
            answer = answer[:len(answer)-1]

    # 5단계 빈 문자열인 경우 'a' 대입
    if len(answer) == 0:
        answer = 'a'
    print(answer)

    # 6단계 길이가 16자 이상이면 첫 15개의 문자를 제외한 나머지 문자를 모두 제거
    # 만약 제거 후 마침표가 끝에 위치하면 마침표 제거
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:len(answer)-1]

    # 7단계 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복하기
    while len(answer) < 3:
        answer += answer[-1]

    return answer