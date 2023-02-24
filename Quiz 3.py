# Quiz 3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리(nav) + 글자 개수(5) + 글자 내 'e' 개수(1) + "!"로 구성
# 예) 생성된 비밀번호 : nav51!

# 내가 푼 방법
url1 = "http://naver.com"
re_url1 = url1[7:url1.find(".")]        # 규칙 1, 2에 대한 부분
password = re_url1[:3] + str(len(re_url1)) + str(re_url1.count("e")) + "!"  # 규칙 3에 대한 부분
print(password)

# 다른 풀이
# 11번째 줄 대신 url1.replace("http://", "") 도 가능. 이게 더 깔끔한 듯.