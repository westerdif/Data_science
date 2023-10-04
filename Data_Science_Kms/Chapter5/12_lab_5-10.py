'''
작성일 : 2023년 10월 4일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 사용자가 이벽하는 숫자의 합을 구함
       
       문제분석: 사용자가 입력한 숫자들을 더하는 프로그램
       사용자가 yes라고 답한 동안에만 숫자를 입력받는다.
'''
#합계 저장
total = 0

#반복문 설정
while True:
    #숫자를 입력받는다.
    num = int(input("숫자를 입력하시오 : "))
    #증감식
    total = total + num
    #반복 여부 확인
    answer = input("계속? (yes/no):")
    
    #만약 여부가 true였다면
    if answer == 'yes':
        #반복
        continue
    
    #아니고 만약에 여부가 flase 였다면
    elif answer == 'no':
        #종료
        break
    

#결과 출력
print("총 합계:", total)
