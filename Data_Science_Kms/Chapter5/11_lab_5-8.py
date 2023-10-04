'''
작성일 : 2023년 10월 4일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : while문으로 별 그리기
'''
#터틀 선언
import turtle as t
t.shape("turtle")
t.penup()
t.pendown() # 이동을 마치면 팬 다운
t.speed(10)
i = 0

#반복문 설정
while i < 100:
    t.forward(100)
    t.right(99)
    i = i + 1