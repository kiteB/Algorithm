# 한 줄로 된 간단한 에디터를 구현해보자
# 첫째 줄에 초기에 편집기에 입력되어 있는 문자열이 주어짐.
# 둘째 줄에는 명령어의 개수를 나타내는 정수 M이 주어짐.
# 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력하라.
case = list(input())
N = int(input())
cursor = len(case)

for i in range(N):
    command = list(input())

    # 커서를 왼쪽으로 한 칸 옮김
    if command[0] == 'L':
        if cursor != 0:
            cursor -= 1

    # 커서를 오른쪽으로 한 칸 옮김
    elif command[0] == 'D':
        if cursor != len(command)+1:
            cursor += 1

    # 커서 왼쪽에 있는 문자를 삭제
    elif command[0] == 'B':
        if cursor != 0:
            del case[cursor-1]
            cursor -= 1

    # 문자를 커서 왼쪽에 추가
    elif command[0] == 'P':
        case.insert(cursor, command[2])
        cursor += 1

# 문자열로 합쳐주기
print(''.join(case))