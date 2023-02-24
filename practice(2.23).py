# [문자열]
sentence = """
오늘은 2월 23일이고,
목요일입니다.
"""
print(sentence)



# [슬라이싱]
jumin = "001205-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])     # 0번째부터 2번째 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])    # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])



# [문자열 처리 함수]
python = "Python is Amazing"

# lower() -> 모두 소문자로 변경
print(python.lower()) 

# upper() -> 모두 대문자로 변경
print(python.upper())      

# isupper() -> 대문자이면 True, 소문자이면 False
print(python[0].isupper())

# len() -> 길이를 알려주는 함수 
print(len(python))        

# replace("원래 있던 것", "새로운 것") -> 원래 있던 것을 새로운 것으로 변경
print(python.replace("Python", "Java")) 

index = python.index("n")
print(index)
index = python.index("n", index + 1)    # index + 1인 6의 위치부터 n을 찾게 됨
print(index)

print(python.find("n"))

# find와 index의 차이
print(python.find("Java"))      # find()에서 원하는 값이 없을 때는 -1을 반환함
# print(python.index("Java"))     # index()에서 원하는 값이 없을 때는 오류를 내면서 프로그램을 종료시킴

# count("n") -> n이 몇 개 있는지 세어주는 함수
print(python.count("n"))    



# [문자열 포맷]
print("a" + "b")
print("a", "b")

# 방법 1 - % 이용
print("나는 %d살입니다." % 20)       # d에는 정수만 넣을 수 있음
print("나는 %s를 좋아해요." % "파이썬")  # s에는 문자열을 넣을 수 있음, 문자건 한 글자건 다 가능
print("Apple은 %c로 시작해요." % "A")    # c에는 한 글자만 넣을 수 있음
print("나는 %s색과 %s색을 좋아해요." %("빨간", "파란"))

# 방법 2 - format() 이용
print("나는 {}살입니다.".format(24))
print("나는 {}색과 {}색을 좋아해요.".format("빨간", "파란"))
print("나는 {1}색과 {0}색을 좋아해요.".format("빨간", "파란"))      # 중괄호 안에 숫자가 있으면 format 안에 있는 값을 원하는대로 넣을 수 있음

# 방법 3 - format()과 변수 이용
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 24, color = "노란"))

# 방법 4 - 변수 만들기 (v3.6 이상부터 가능)
age = 24
color = "노란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")