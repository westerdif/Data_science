'''
작성일 : 2023년 9월 20일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 선택문 if
       정수를 입력받아 짝수인지 홀수인지 판단.
       
       짝수는 2로 나눈 나머지 0이다
       홀수는 2로 나눈 나머지 (0이 아니다.)
'''
#정수를 입력받는다.
num = int(input('정수를 입력하시오 : '))

#만약 정수를 2로 나눈 나머지가 0이면
    #"입력받은 정수는 짝수입니다." 출력
if num % 2 == 0:
    print(f"입력받은 정수 {num}는 짝수입니다.")

#아니면
    #입력받은 정수는 홀수입니다.    
else:
    print(f"입력받은 정수 {num}는 홀수입니다.")
