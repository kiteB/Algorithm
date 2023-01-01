# 학생 5명의 기말고사 시험 점수가 주어졌을 때, 평균 점수를 구하여라.
# 단, 성적이 40점 미만인 경우에는 보충 학습을 듣는 조건을 수락하면 40점을 받게 된다.
# 보충 학습은 거부할 수 없기 때문에, 40점 미만인 학생들을 항상 40점을 받게 된다.
import sys

scores = []
for _ in range(5):
    score = int(sys.stdin.readline())
    if score < 40:
        score = 40
    scores.append(score)

print(round(sum(scores)/5))
