# 여우는 어떻게 울지?
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    animal_sounds = list(sys.stdin.readline().split())
    sounds = []

    while True:
        case = sys.stdin.readline().strip()

        if case == 'what does the fox say?':
            break

        animal, goes, sound = case.split()
        sounds.append(sound)

    answer = []
    for i in animal_sounds:
        if i not in sounds:
            answer.append(i)
    print(*answer)
