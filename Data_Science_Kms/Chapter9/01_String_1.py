'''
작성 : 2023년 11월 15일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 
'''
# 문자열 슬라이싱
s  ='Happy day!'
print(s[0])
print(s[6:10])
print(s[:-2])

# 문자열 분리 : split() - 괄호 완에 있는 것을 기준으로 분리
s = 'Welcome to Python'
print(s.split()) # 공백을 기준으로 분리 (리스트와 문자열은 같다 그리고 공백 또한 문자열이다.)

s = '2023.11.15'
print(s.split('.'))

s = 'Hello, World'
print(s.split(','))

s = 'Hello, World'
print(s.split(',  '))


# 공백 제거 : strip()
s = 'Welcome, to, Python, and, bla, bla        '
print(s.strip())
print([X.strip() for X in s.split(',')])

print(list('Hello, World!'))


# 문자열 연결 : join()
print(','.join(['apple', 'grape', 'banana'])) # ','을 붙여서 연결하라
print('-'.join('010.1234.5678'.split('.'))) #'.'을 기준으로 구분되누번호를 -로 고친다.

# . 을 - 로 바꾸기
print('010.1234.5678'.replace('.','-'))

s = 'Hello, World!'
print(s)
# 리스트로 문자열 분이 시켜 s_list에 저장.
s_list = list(s)
print(s_list)
# 분리된 문자를 다시 합치기
print(''.join(s_list))

# 줄 바꿈과 탭이 포함된 문자열 그대로 출력
a_string = 'Today as Well, \n\t Have a Happy Day'
print(a_string)

# 문자열 자르기 word_list에 저장
word_list = a_string.split()
print(word_list)

# 다시 합치기 - 문자열을 자르고 다시 합치면 줄바꿈과 탭이 삭제됨
refined_string = " ".join(word_list)
print(refined_string)

# 대소문자 변환과 문자열 삭제
s = 'Hello, World!'
print(s.lower()) # lower() - 소문자로 변환
print(s.upper()) # upper() - 대문자로 변환

# 공백 제거 strip()
s = '              Hello, World!                 '
print(s.strip()) # 왼쪽, 오른쪽 모든 공백 제거
print(s.lstrip())
print(s.rstrip())

s = '#####################Hello, World!#######################'
print(s)
print(s.strip('#'))

# 문자열 찾기
s = 'WWW.silla.ac.kr'
print(s.find('.kr')) # find() - 괄호 안에 있는 문자의 번지 수를 찾음
print(s.find('X')) # -1(문자열이 없다는 뜻)
print(s.count('.')) # '.'의 개수