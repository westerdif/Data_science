'''
작성일 : 2023년 10월 11일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 함수에 일을 시키고 그 값을 받아오기
       
       
       원의 넓이 구하기
       반지름이 3인 원의 넓이를 구한다.
       바지름 값을 전달받아 원의 넓이를 구하고 넓이를 돌려주는 함수를 작성
'''
#함수선언
def area(num):
    result = num * num *3.14
    return result

#함수호출
result = area(3)
print(f"잔지름이 3인 원의 넓이는 {result}입니다.")

print("================================")

#함수선언
def area(num):
    result = num * num *3.14
    return result

#함수호출
num = int(input("반지름을 입력하시오 : "))
result = area(num)
print(f"잔지름이 {num}인 원의 넓이는 {result}입니다.")


print(f"잔지름이 {num}인 원의 넓이는 {area(num)}입니다.") #반지름을 가지고 함수 호출하고, 전달받아 바로 출력
