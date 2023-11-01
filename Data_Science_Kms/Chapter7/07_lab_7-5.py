'''
작성일 : 2023년 11월 1일 
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : lab 7-5 함수는 튜플을 돌려줄 수 있다.   
       

       반지름을 입력받아 원의 넓이와 둘레를 계산하시오.
       넓이와 둘레를 계산하는 함수를 작성하시오.
       함수는 넓이와 둘레를 함께 돌려줍니다.

       [함수]
       #반지름을 받는다. 매개변수에 저장
       #넓이와 둘레를 구한다.
       #넓이와 둘레를 반환한다.

       [메인]
       #반지름을 입력받는다.
       #함수 호출
       #반환받은 값을 튜플로 저장
       #결과 출력
'''
import math

#함수 정의
import math

#넓이와 둘레를 계산하는 함수 정의
def calculate(radius):
    #원의 넓이
    area = math.pi * radius ** 2  
    #원의 둘레
    circumference = 2 * math.pi * radius  
    #튜플로 반환
    return area, circumference  

#메인 
# 반지름 입력 받기
radius = float(input("반지름을 입력하세요: "))  
# 함수 호출
area, circumference = calculate(radius)  
print(f"반지름이 {radius}인 원의 넓이는 {area:.2f} 이고, 둘레는 {circumference:.2f} 입니다.")
