def solution(s):
    if len(s) == 1:
        return 1

    cnt = 0
    print(len(s)//2)

    # 1부터 len(s)//2 까지 문자열을 잘라보기
    for unit in range(1, len(s)//2+1):
        print(f'unit: {unit}')

        for i in range(0, len(s), unit):
            print(i, end=' ')
            first_idx = i+unit
            second_idx = first_idx + unit
            # print(f'first_idx: {first_idx}, second_idx: {second_idx}')
            # print(f'first: {s[i:first_idx]}', end=' / ')
            # print(f'second: {s[first_idx:second_idx]}')
            # print()
            # print(f'i: {i}, i+unit: {i+unit}')
            # print(s[i:(i+unit)])
            # print(f'{s[i:(i+unit)]}, {s[(i+unit+1):(i+unit*2)]}')

            # 문자열 압축이 가능한 경우
            if s[i:first_idx] == s[first_idx:second_idx]:
                print(f'first_idx: {first_idx}, second_idx: {second_idx}')
                print(f'first: {s[i:first_idx]}', end=' / ')
                print(f'second: {s[first_idx:second_idx]}')
                print(f'압축!')
                print()

                # 이전에 압축했던 경우
                if i != 0 and s[i-1].isdigit():
                    s[i-1] += 1
                    s[i:second_idx].replace(s[i:second_idx], s[i:first_idx])
                else:
                    s[i:second_idx].replace(s[i:second_idx], '2' + s[i:first_idx])

            print(f's: {s}')
            #     # s[i:(i+unit*2)].replace(s[i:(i+unit*2)], )
            #     cnt += 1
            #     print(f'{s[i:(i+unit)]} == {s[(i+unit):(i+unit*2)]}')
            # # else:
            #     # print(f'{s[i:(i+unit)]} == {s[(i+unit):(i+unit*2)]}')
        # print(cnt)


solution("aabbaccc")