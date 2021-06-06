from collections import Counter

case = input().upper()

if len(case) == 1:
    print(case)
else:
    counter = Counter(case).most_common(2)
    if counter[0][1] == counter[1][1]:
        print('?')
    else:
        print(counter[0][0])