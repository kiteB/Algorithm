# Lv.2 | 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    # 1. 오름차순으로, 2. 길이가 짧은 순서대로 정렬
    phone_book = sorted(phone_book, key=lambda x: (x, len(x)))

    # phone_book의 연속된 두 개의 요소(p1, p2)를 비교
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
