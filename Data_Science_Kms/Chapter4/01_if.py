'''
작성일 : 2023년 9월 20일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 선택문 if
       성적을 입력받아 60점 이상이라면 "합격입니다"출력
'''
#성적을 입력받는다.
score = int(input('성적을 입력하시오 : '))

#만약 성적이 60점이상이라면 "합격입니다." 출력
if score >= 60:
    print("합격입니다.")
#아니면"불합격입니다."
else:
    print("불합격입니다.")


print("==================================")


'''
자동차의 속도를 입력받아 속도를 출력하소
30km/h이면 "과속입니다. 속도를 줄이세요." 출력하고,
속도와 상관없이 "안전 운전하세요." 출력
'''
#자동차의 속도를 입력받는다.
speed = int(input('자동차의 속도를 입력하시오. : '))

#입력받은 속도를 출력하고
print("현재 자동차의 속력은 : {}km/h" .format(speed))
print(f"현재 자동차의 속력은 : {speed}km/h") #더 효율적효율적

#만약 속도가 30km/h이면 "과속입니다. 속도를 줄이세요." 출력
if speed >= 30:
    print("과속입니다. 속도를 줄이세요.")

#아니명 "안전 운전하세요." 출력
else:
    print("안전 운전하세요.")