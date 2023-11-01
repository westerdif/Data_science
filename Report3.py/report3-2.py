'''
작성 : 2023년 00월 00일
학번 : 202395001
학과 : 컴퓨터공학부
이름 : 구민수
설명 :  1~100 사이의 10개의 랜덤수로 리스트를 생성합니다.
        리스트에 저장된 수 중에서 홀수만 리스트에 저장합니다.
        랜덤 생성된 리스트와 홀수 리스트는 오름차순으로 정렬하여 출력하고, 홀수 리스트에 저장된 홀수의 개수도 출력합니다.
        랜덤수 저장 변수 : num1_본인학번
        홀수 저장 변수 : num2_본인학번
'''
#랜덤 모듈 선언
import random

#반복문을 사용, 1~100사이의 10개의 랜덤수를 저장하는 리스트 생성
num1_202395001 = []
for i in range(10) :
    num1_202395001.append(random.randint(1,100))

#홀수만 추출하여 리스트에 저장
num2_202395001 = []
for num in num1_202395001:
    if num % 2 != 0:
        num2_202395001.append(num)

#리스트 정렬
num1_202395001.sort()
num2_202395001.sort()

#결과 출력
print(f"랜덤 생성된 리스트 (num1_202395001): {num1_202395001}")
print(f"홀수 리스트 (num2_202395001): {num2_202395001}")
print(f"홀수의 개수: {len(num2_202395001)}")