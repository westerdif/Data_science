'''
작성일 : 2023년 9월 13일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 1장
'''
import turtle as t #turtle 모듈을 사용하기 위한 준비
                   #turtle 클래스 객체를 t로 생성. (별명)
                   

t.shape('turtle')
t.speed(2)
#선 그리기

#t.forward(200)  #200PX 이동


#삼각형 그리깃.
'''
t.forward(200)  #200PX 이동
t.left(120)  #왼쪽으로 60도 회전
t.forward(200)  #200PX 이동
t.left(120)  #왼쪽으로 60도 회전
t.forward(200)  #200PX 이동
t.left(120)  #왼쪽으로 60도 회전
'''


for i in range(5):
    t.forward(100)  #200PX 이동
    t.left(144)  #왼쪽으로 60도 회전
    
t.mainloop()  #계속 진행