# 후보 추천하기
import sys

n = int(sys.stdin.readline())           # 사진틀 개수
total_cnt = int(sys.stdin.readline())   # 총 추천 개수
students = list(map(int, sys.stdin.readline().split()))     # 추천 받은 학생 리스트

frames = {}     # 사진틀 정보

for idx, student in enumerate(students):

    if student in frames:       # frames에 존재하는 학생이라면 추천 횟수 증가시켜주기
        frames[student][0] += 1
    else:
        if len(frames) < n:     # frames 개수가 n보다 작다면, frames[학생번호] = [1, 인덱스]
            frames[student] = [1, idx]
        else:   # frames 개수가 n보다 크거나 같다면, 가장 오래된 사진을 삭제해야 한다.
            tmp = sorted(frames.items(), key=lambda x: [x[1][0], x[1][1]])
            oldest = tmp[0][0]
            del frames[oldest]  # 가장 오래된 사진 삭제
            frames[student] = [1, idx]  # 새로 추천받은 학생 정보 추가

answer = list(sorted(frames.keys()))
print(str(' '.join(map(str, answer))))
