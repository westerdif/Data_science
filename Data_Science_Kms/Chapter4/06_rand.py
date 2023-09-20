'''
작성일 : 2023년 9월 20일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 선택문 if
       random 을 이용한 가위바위보 게임
       
       random  함수로 생성된 정수를 가지고 게임을 한다
       0 = 가위
       1 = 바위
       2 = 보
'''
#랜덤 선언
import random

print("가위바위보 게임 시작")

npc = random.randrange(3)

if npc == 0:
    print("가위")
if npc == 1:
    print("바위")
if npc == 2:
    print("버")