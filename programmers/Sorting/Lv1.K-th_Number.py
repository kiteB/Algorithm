def solution(array, commands):
    arr = array
    answer = []
    for each in commands:
        i, j, k = each[0], each[1], each[2]
        numbers = sorted(arr[i-1:j])
        answer.append(numbers[k-1])
    return answer