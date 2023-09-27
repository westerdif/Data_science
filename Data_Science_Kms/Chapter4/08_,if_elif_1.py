'''
작성일 : 2023년 9월 27일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 점수를 입력하여 학점을 구하시오
'''
#점수를 입력받는다.
score = int(input("점수를 입력하시오 : "))

#만약 점수가 0점이상 100이하라면
    #학점계산
if score >= 0 and score <= 100:
    
    #만약 점수가 90점 이상이면
        #A학점 출력
    if score >= 90:
        print(f"{score}는 A학점입니다.")

    #아니고 만약 점수가 80점 이상이면
        #B학점 출력
    elif score >= 80:
        print(f"{score}는 B학점.")

    #아니고 만약 점수가 70점 이상이면
        #C학점 출력
    elif score >= 70:
        print(f"{score}는 C학점.")

    #아니고 만약 점수가 60점 이상이면
        #D학점 출력
    elif score >= 60:
        print(f"{score}는 D학점.")

    #아니고 만약 점수가 50점 이상이면
        #E학점 출력
    elif score >= 50:
        print(f"{score}는 E학점.")

    #아니면
        #F학점 출력
    else:
        print(f"{score}는 F학점.")
        
#아니면 
    #잘못된 방식입니다. 출력
else:
    print("잘못된 방식입니다.")
    
print("===========================================")

# 점수를 입력받는다.
score = int(input("점수를 입력하시오: "))

# 점수 범위를 확인한다.
if 0 <= score <= 100:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"{score}는 {grade}학점입니다.")
else:
    print("잘못된 방식입니다.")
  