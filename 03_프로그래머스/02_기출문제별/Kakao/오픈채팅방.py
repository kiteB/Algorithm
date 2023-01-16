# 오픈 채팅방
def solution(record):
    answer = []
    users = {}          # 유저의 아이디와 닉네임을 저장할 딕셔너리
    results = []        # action과 유저 아이디를 저장할 리스트

    for r in record:
        case = r.split()
        action, uid = case[0], case[1]      # 액션과 유저 아이디 분리

        # action이 "Enter"나 "Change"인 경우, uid에 해당 이름 지정
        if action == 'Enter' or action == 'Change':
            new_id = case[2]
            users[uid] = new_id

        results.append([action, uid])

    for result in results:
        action, uid = result[0], result[1]

        if action == 'Enter':
            answer.append(users[uid] + "님이 들어왔습니다.")
        elif action == 'Leave':
            answer.append(users[uid] + "님이 나갔습니다.")

    return answer