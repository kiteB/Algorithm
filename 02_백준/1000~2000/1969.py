# DNA
import sys

n, m = map(int, sys.stdin.readline().split())
dna = [sys.stdin.readline().strip() for _ in range(n)]

dna_to_num = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
num_to_dna = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

answer = ''
hamming_distance = 0

for j in range(m):
    count = [0] * 4

    for i in range(n):
        count[dna_to_num[dna[i][j]]] += 1

    max_dna = max(count)
    max_dna_idx = count.index(max_dna)

    answer += num_to_dna[max_dna_idx]
    count[max_dna_idx] = 0  # 초기화
    hamming_distance += sum(count)

print(answer)
print(hamming_distance)