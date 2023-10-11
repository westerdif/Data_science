'''
작성일 : 2023년 10월 11일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 함수에 여러개의 값 넘겨주기
       
       두 수를 입력받아 함수를 호출하여 두 수 사이의 합을 계산하여 돌려주는 함수
       
       [알고리즘]
       (함수)
        두 수를 전달받아 매개변수에 저장한다.
        두 수 사이의 합을 계산한다.
        계산된 합을 함수를 호출한 곳으로 돌려준다. ~
       
       (메인)
        두 수를 입력받는다.
        두 수를 가지고 함수를 호출한다.
        ~ 돌려받은 합을 출력한다.
'''
print("두 수 사이의 합을 구하기(매개변수가 2인 함수)")
def get_sum(num1, num2):
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
        # 두 수 사이의 합계 초기화
        total = 0

        # 두 수 사이의 합계 계산
        while start >= end:
            total += start
            
            start -= 1
            
    #값 반환
    return total

#함수호출
num1 = int(input("시작 수를 입력하시오 : "))
num2 = int(input("종료 수를 입력하시오 : "))
total = get_sum(num1, num2) 
print(f"{num1}와 {num2} 사이의 수의 합은 {total}")    
print(f"{num1}와 {num2} 사이의 수의 합은 {get_sum(num1, num2)}")   #함수를 바로 호출하여 값 바로 출력