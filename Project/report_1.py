'''
학과 : 컴퓨터공학부
학번 :
설명 : 사용자로부터 나이를 입력받아 20살이상이면 "Adult", 10살 이상 20살미만이면 "youth", 10살미만이면 "kid"로 출력하는 프로그램 작성
'''
#나이를 입력받는다.
age = int(input("나이를 입력하시오 : "))

#만약 나이가 20살이상이면 
    # "Adult" 출력
if age >= 20:
    print(f"사용자의 나이가 {age}이므로 Adult입니다.")

#만약 나이가 10살이상 20살 미만이면 
    # "Youth" 출력
if age >= 10 and age < 20:
    print(f"사용자의 나이가 {age}이므로 youth입니다.")

#아니면
    # "Kid" 출력
else:
    print("kid입니다.")