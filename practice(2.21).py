# [주석 처리 한번에 하는 방법]
# -> ctrl + /



# [연산자]
print(1+1)
print(4-2)
print(5/3)
print(5//3)     # 몫 구하기
print(5%3)      # 나머지 구하기
print(1 == 1)
print(1 != 3)
print(not(1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 > 5))    # & = and

print((3 > 0) or (3 < 5))
print((3 > 0) | (3 > 5))    # | = or

print(5 > 4 > 3)
print(5 > 4 > 7)



# [숫자 처리 함수]
# abs() -> 절대값
print(abs(-5))

# pow() -> 제곱
print(pow(4, 2))    # 4^2

# max() -> 최대값
print(max(5, 12))

# min() -> 최소값
print(min(5, 12))

# round() -> 반올림
print(round(3.14))
print(round(4.99))

from math import *      # math 라이브러리 안에 있는 모든 것을 이용하겠다는 의미
# floor() -> 내림
print(floor(4.99))

# ceil() -> 올림
print(ceil(3.14))       

# sqrt() -> 제곱근
print(sqrt(16))         



# [랜덤함수]
from random import *
# random() -> 0.0 이상 1.0 미만의 임의의 값 생성
print(random())
print(random() * 10)    # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random() * 10))   # 0 이상 10 미만의 임의의 값 생성

# randrange(a, b) -> a 이상 b 미만의 임의의 값 생성
print(randrange(1, 46))

# randint(a, b) -> a 이상 b 이하의 임의의 값 생성
print(randint(1, 45))