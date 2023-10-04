'''
작성일 : 2023년 10월 4일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 조건에 따라 반복하는 while문
'''
#while 조건식:
#   들여쓰기로 반복하면서 할일 작성
#반복문에서는 반드시 종료조건이 있어야한다.
#while True => 무한반복

under_construction = True  #공사중

while under_construction:
    response = input("공사가 완료되었습니까? : ")
    if response == '예':
        under_construction = False
        
print("루프 탈추리!!!")