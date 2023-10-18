'''
작성일 : 2023년 10월 18일 
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 리스트의 객체 생성과 참조
'''
fruits1 = ['딸기', '수박', '레몬']

fruits2 = fruits1

print("fruits1 :", fruits1)
print("fruits2 :", fruits2)

fruits2[1] = '망고'  #지정한 항목의 변경

print("fruits1 :", fruits1)  #모두 1번지 내용으로 망고로 바뀐다.
print("fruits2 :", fruits2)  #주소를 참조하기 때문(같은 주소)

#주소 학인 => 메모리 위치 정보 알아보기 id()함수
print("fruits1의 id :", id(fruits1))
print("fruits2의 id :", id(fruits2)) #두 리스트의 아이디가 같다.

'''
    리스트의 내용 복제  list() 함수
'''
fruits2 = list(fruits1) #내용 복제(배정)
print(":: 내용 복제 후 1 ::")
print("fruits1 :", fruits1)
print("fruits2 :", fruits2)

print("fruits1의 id :", id(fruits1))
print("fruits2의 id :", id(fruits2))

#내용 복제 2
fruits3 = fruits1[:]
print(":: 내용 복제 후 2 ::")
print("fruits1 :", fruits1)
print("fruits2 :", fruits2)

print("fruits1의 id :", id(fruits1)) #id 정보가 다르다
print("fruits3의 id :", id(fruits3))

fruits3[0] = '수박'
print(":: fruits의 0번지에 수박으로 내용 바꾼 후 ::")
print("fruits1 :", fruits1)
print("fruits3 :", fruits3)