# 파일 정리
import sys

n = int(sys.stdin.readline())
files = {}

for _ in range(n):
    file = sys.stdin.readline().strip()
    name, extension = file.split('.')

    if extension in files:
        files[extension] += 1
    else:
        files[extension] = 1

files = sorted(files.items(), key=lambda x: x[0])
for key, val in files:
    print(key, val)