'''
작성일 : 2023년 9월 20일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 선택문 if
       교통 카드의 종류로 '청소년', '성인' 카드가 있다고 하자.
       사용자에게 카드의 종류를 입력받아 청소년이면 '청소년입니다.' 출력
       '성인이면' '성인입니다' 출력
'''
#교통 카드를 입력받는다.
passcard = input('카드 정보를 입력하시오 : ')

#만약 교통카드가 청소년 카드라면
    #"청소년입니다." 출력
if passcard == '청소년':
    print("청소년입니다")
    
#아니면
    #"성인입니다." 출력
else:
    print("성인입니다.")
    
print("=================================")

card_type = input("카드 정보를 입력하시오 : ")

if card_type == '청소년' and '성인':
    if card_type == '청소년':
        print("청소년입니다.")
        
    else:
        print("성인입니다.")
        
else:
    print("잘못된 정보입니다.")

print("=================================")

card_type = input('카드 정보를 입력하시오 : ')

if card_type == '미성년' and '성인':
    if card_type == '미성년':
        pupil = input('자신이 속한 분류를 선택하십시오 : ')
        if pupil == '어린이':
            print("사용자님은 어린이입니다")
            print("사용자님의 교통 금액은 700원입니다.")
        
        else:
            print("사용자님은 청소년입니다.")
            print("사용자님의 교통 금액은 1100원입니다")
            
        
    else:
        print("사용자님은 성인입니다.")
        print("사용자님의 교통 금액은 1500원입니다")
        
else:
    print("현재 입력하신 정보는 잘못된 정보입니다.")