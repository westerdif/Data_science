'''
작성일 : 2023년 9월 27일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : range() 함수
'''
for i in range(3):
    print(i, end='. ') #end쓰면 줄바꿈 하지 않는다.(연결)
    print("안녕하세요")
    print("   구민수입니다.")

#range(시작값, 숫자 앞까지, 증가값(감소값))
for i in range(1, 6):
    print(i, end=' ')
    
print()
    
#10~1까지
for i in range(10, 0, -1):
    print(i, end=' ')