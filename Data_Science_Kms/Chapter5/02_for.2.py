'''
작성일 : 2023년 9월 27일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 반복문 for 사용
'''
#본인 이름 5번 출려
for i in range(5):
    print(i,"구민수")
    
#리스트
for i in [1,2,3,4,5]:
    print(i,"구민수")
    
print("리스트로 구구단 19단 출력")
for num in [1,2,3,4,5,6,7,8,9]:
    print(f"19 * {num} = {19*num}")
    
print("문자열 내용 출력")
for i in "hello":
    print("i =", i) #i값 출력
    
print("bts 멤버 출력")
bts = ["뷔", "제이홉", "알엠", "정국", "진", "지민", "슈가",]

for i in bts:
    print("멤버 : ",i)