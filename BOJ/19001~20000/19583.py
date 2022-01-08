# 싸이버개강총회
import sys

s, e, q = sys.stdin.readline().split()
s = int(''.join(s.split(":")))
e = int(''.join(e.split(":")))
q = int(''.join(q.split(":")))

members = {}  # 채팅 정보 저장
answer = 0
while True:
    line = sys.stdin.readline()

    if len(line) < 5:   # 제대로 된 입력이 들어오지 않으면 종료
        break

    time, nickname = line.split()
    time = int(''.join(time.split(":")))

    if time <= s:  # 개총 시작 전에 채팅 기록이 있다면
        members[nickname] = 1
    elif e <= time <= q:  # 개총 종료 ~ 스트리밍 종료 시간 안에 채팅 기록이 있다면
        if members.get(nickname) == 1:
            answer += 1
            members[nickname] += 1  # 중복으로 체크하는 것을 방지하기 위해

print(answer)
