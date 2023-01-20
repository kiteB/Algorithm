# 나는야 포켓몬 몬스터 이다솜
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon_dict = dict()

for idx in range(1, n + 1):
    pokemon = input().strip()
    pokemon_dict[pokemon] = idx
    pokemon_dict[str(idx)] = pokemon    # 포켓몬 번호 입력 시 따로 검사하지 않기 위해서 str 값을 키로 설정

for i in range(1, m + 1):
    print(pokemon_dict[input().rstrip()])
