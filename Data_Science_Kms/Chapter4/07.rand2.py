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
       
       두개의 플레이어의 이름을 입력받아 가위바위보 게임을 진행합니다.
'''
import random

print("가위바위보 게임 시작")

player1 = input('player1의 이름 : ')
player2 = input('player2의 이름 : ')

npc1 = random.randrange(3)
npc2 = random.randrange(3)

print(player1, " : ", end='')
if npc1 == 0:
    print("가위")
elif npc1 == 1:
    print("바위")
else:
    print("보")

print(player2, " : ", end='')
if npc2 == 0:
    print("가위")
elif npc2 == 1:
    print("바위")
else:
    print("보")

print("===========")
print("게임의 승자는")
if npc1 == npc2:
    print("무승부입니다")
else:
    if (npc1 == 0 and npc2 == 2) or (npc1 == 1 and npc2 == 0) or (npc1 == 2 and npc2 == 1):
        print(player1,"의 승리")
    else:
        print(player2,"의 승리")
