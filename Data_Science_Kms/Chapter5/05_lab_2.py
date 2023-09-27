'''
작성일 : 2023년 9월 27일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 터틀 그래픽으로 n각형 도형
       사용자로부터 그리고싶은 도형의 변의 수를 입력받아 도형을 그린다.
'''
import turtle as t

t.shape("turtle")

#팬 이동 - 펜 자국이 남지 않도록 들어서 이동
t.penup()
t.goto(-50, -50)
t.pendown() # 이동을 마치면 팬 다운

#원하는 도형을 입력받는다.
    
for i in range(5):
    pel = int(t.textinput('도형그리기', '몇각형의 도형을 그릴까요? : '))
    
    for i in range(pel):
        t.forward(50)
        t.left(360/pel)