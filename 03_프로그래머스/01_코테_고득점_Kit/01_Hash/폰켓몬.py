# 폰켓몬
def solution(nums):
    set_nums = set(nums)
    cnt = len(nums) / 2
    answer = len(set_nums)

    return min(answer, cnt)