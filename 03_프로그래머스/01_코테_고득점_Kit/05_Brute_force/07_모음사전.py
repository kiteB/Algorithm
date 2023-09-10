# Lv.2 | 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product


def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']

    # product를 사용하여 중복 조합 생성 - `repeat=n`를 활용하여 n번씩 원소를 뽑아서 생성
    words = [''.join(list(p)) for cnt in range(1, 6) for p in product(vowels, repeat=cnt)]
    words.sort()

    return words.index(word) + 1
