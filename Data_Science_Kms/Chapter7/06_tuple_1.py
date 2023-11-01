'''
작성 : 2023년 11월 1일 
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 :  한 번 생성하면 그 값을 고칠 수 없는 자료형 : 튜플
'''
#리스트 생성
color_list = ['red', 'green', 'blue', 'orange']

#튜플 생성
color = ('red', 'green', 'blue', 'orange')

#튜플 출력
print(f"color : {color}")

#color에 black을 추가
#튜플은 추가 및 삭제가 안된다.
#color.append('black')

#인덱싱과 슬라이싱은 문자열이나 이스트와 동일하게 동작한다.
print("color 튜플 : ", color)
print("color 튜플 중 2,3,4번은 ?: ", color[1:4])
print("color 튜플 중 1,2,3번은 ?: ", color[:3])
print("color 튜플 중 3번~끝까지는 ?: ", color[2:])
print("color 튜플 중 1,3,5번은 ?: ", color[::2])
print("color 튜플 중 거꾸러 출력: ", color[::-1])

#튜플끼리의 결합 => + 연산자,  반복 => * 연산자
colors = color + color
print("colors 튜플 : ", colors)
colors = color *10
print("colors 튜플(10번 반복) : ", colors)