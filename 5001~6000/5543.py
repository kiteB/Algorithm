# 햄버거집에서 햄버거와 음료를 세트로 구매하면 50원을 뺀 가격이 세트 메뉴의 가격이다.
# 햄버거와 음료의 가격이 주어졌을 때, 가장 싼 세트 메뉴의 가격을 출력하는 프로그램을 작성하시오.
import sys

burger = []
drink = []
for _ in range(3):
    burger.append(int(sys.stdin.readline()))

for _ in range(2):
    drink.append(int(sys.stdin.readline()))

print(min(burger)+min(drink)-50)

