def solution(numbers):
    lst = list(map(str, numbers))
    lst2 = sorted(lst, key=lambda x: x*3, reverse=True)
    return str(int(''.join(lst2)))