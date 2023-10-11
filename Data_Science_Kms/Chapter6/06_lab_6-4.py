'''
작성일 : 2023년 10월 11일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수.
       
       리스트에 10개의 값을 랜덤으로 생성하고,
       max 또는 min을 입력받아 최대, 최소값을 찾아 돌려주는 함수
       
       [알고리즘]
       (함수)
        -값을 입력받아 매개변수에 저장
        -최대값, 최소값을 찾는다. max()함수, min()함수 사용
        -값을 반환한다.
       
       
       (메인)
        무한반복
            -랜덤으로 10~99까지 10개의 수를 리스트로 생성
            -생성된 리스트를 출력
            -사용자로부터 최대값을 알고 싶은지 최소값을 알고 싶은지 묻는다.
                #사용자가 입력할 것은 max 또는 min,
            -입력받은 max 또는 min생성된 리스트를 가지고 함수 호출
            반환받은 최대값 또는 최소값을 출력
'''
import random

# 최대값 또는 최소값을 찾아 반환하는 함수 정의
def find(numbers, opt):
    #만약 선택이 최대라면
    if opt == "max":
        #최대값 검색
        result = max(numbers)
        #아니고 만약 최소라면
    elif opt == "min":
        #최소값 검색
        result = min(numbers)
        #아니면
    else:
        result = None
        
    #값 반한
    return result

#무한반복
while True:
    # 10개의 10부터 99까지 무작위 숫자를 생성하여 리스트로 저장
    random_numbers = [random.randint(10, 99) for i in range(10)]

    print("생성된 무작위 숫자 리스트:", random_numbers)

    #질문
    user_option = input("최대값 또는 최소값을 무엇을 선택하시겠습니까? (max 또는 min을 입력하세요, 나가려면 'esc' 입력): ")

    #esc를 입력하면 종료
    if user_option == "esc":
        break

    #함수호출
    result = find(random_numbers, user_option)

    #결과 출력
    if result is not None:
        print(f"{user_option} 값은 {result} 입니다.")
    else:
        print("올바른 옵션을 입력하세요 (max 또는 min).")
