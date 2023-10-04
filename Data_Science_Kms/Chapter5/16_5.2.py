'''
작성일 : 2023년 10월 4일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : while문 사용
       두 수를 입력받아
       두 수 사이의 합계를 출력
       두 수 사이의 짝수의 합께를 출력
       
       필요변수 : num1, num2
'''
# 두 수 입력 받기
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

# 두 수 중 큰 수와 작은 수를 구분
if num1 > num2:
    start = num1
    end = num2
else:
    start = num2
    end = num1

# 두 수가 같으면 예외 처리
if start == end:
    print("두 수가 동일합니다. 다른 수를 입력하세요.")
else:
    # 두 수 사이의 합계와 짝수의 합계 초기화
    total = 0
    even_total = 0

    # 두 수 사이의 합계 및 짝수의 합계 계산
    while start >= end:
        total += start
        if start % 2 == 0:
            even_total += start
        start -= 1

    # 결과 출력
    print(f"{num1}와 {num2} 사이의 합계는 {total}입니다.")
    print(f"{num1}와 {num2} 사이의 짝수의 합계는 {even_total}입니다.")

