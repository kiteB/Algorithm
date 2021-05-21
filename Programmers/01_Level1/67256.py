# 키패드 누르기


def solution(numbers, hand):
    answer = ''
    keypad = {1: [0, 0], 2: [1, 0], 3: [2, 0],
              4: [0, 1], 5: [1, 1], 6: [2, 1],
              7: [0, 2], 8: [1, 2], 9: [2, 2],
              10: [0, 3], 0: [1, 3], 12: [2, 3]}
    thumb = [[0, 3], [2, 3]]                # 엄지손가락의 현재 위치

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            thumb[0] = keypad[i]
        elif i in [3, 6, 9]:
            answer += 'R'
            thumb[1] = keypad[i]
        else:
            # 거리 계산
            abs_left = abs(keypad[i][0] - thumb[0][0]) + abs(keypad[i][1] - thumb[0][1])
            abs_right = abs(keypad[i][0] - thumb[1][0]) + abs(keypad[i][1] - thumb[1][1])

            if abs_left < abs_right:
                answer += 'L'
                thumb[0] = keypad[i]

            elif abs_left > abs_right:
                answer += 'R'
                thumb[1] = keypad[i]

            else:
                if hand == 'left':
                    answer += 'L'
                    thumb[0] = keypad[i]

                elif hand == 'right':
                    answer += 'R'
                    thumb[1] = keypad[i]

    return answer