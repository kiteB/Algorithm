# [1차] 비밀지도
def solution(n, arr1, arr2):
    answer = []
    bin1 = []               # arr1을 이진수로 변환한 값을 담을 리스트
    bin2 = []               # arr2를 이진수로 변환한 값을 담을 리스트

    for i in range(n):
        bin1.append(bin(arr1[i])[2:])
        bin2.append(bin(arr2[i])[2:])

        # 길이가 n이 되도록 bin 리스트 채우기
        bin1[i] = '0' * (n - len(bin1[i])) + bin1[i]
        bin2[i] = '0' * (n - len(bin2[i])) + bin2[i]

        tmp = ''
        for j in range(n):
            if bin1[i][j] == '1' or bin2[i][j] == '1':
                tmp += '#'
            elif bin1[i][j] == '0' and bin1[i][j] == '0':
                tmp += ' '
        answer.append(tmp)

    return answer