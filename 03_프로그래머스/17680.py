# 캐시 - 23분
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize > 0:
        for city in cities:
            city = city.lower()     # 모두 소문자로 변환

            # cache hit -> 실행 시간 1
            if city in cache:
                cache.remove(city)          # 기존 cache에서 city 제거
                cache.append(city)          # cache 맨 끝에 city 추가
                answer += 1
            else:       # cache miss -> 실행 시간 5
                if len(cache) < cacheSize:  # 캐시 사이즈보다 작으면 맨 뒤에 추가
                    cache.append(city)
                else:                       # 캐시 사이즈보다 같거나 크면 맨 앞 제거, 맨 뒤 추가
                    cache.popleft()
                    cache.append(city)
                answer += 5
    else:   # 캐시 크기 0이면 모두 cache miss!
        answer = len(cities) * 5
        
    return answer