# 학점계산
import sys

grade = sys.stdin.readline().strip()
grade_dict = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}

answer = grade_dict[grade[0]]
if grade[0] == 'F':
    print(answer)
else:
    if grade[1] == '+':
        answer += 0.3
    elif grade[1] == '-':
        answer -= 0.3
    print(answer)