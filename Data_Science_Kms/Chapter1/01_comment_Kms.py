'''
작성일 : 2023년 9월 13일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 1장
'''
#학과 학번 이름을 저장하시오
major = input('학과를 입력하시오 : ')
id = input('학번 입력하시오 : ')
name = input('이름 입력하시오 : ')

#출력한다.
print("학과 : ", major)
print("학과 : {}" .format(major))
print("학번 : ", id)
print("학번 : {}" .format(id))
print("이름 : ", name)
print("이름 : {}" .format(name))

#안녕하세요. 저는 00학과 00학번입니다.
print("안녕하세요. 저는 {}학과 {}학번 {}입니다." .format(major,id,name))
print("안녕하세요. 저는", major, "학과", id , "학번", name , "입니다.")

#파이썬을 출력하시오. 반복분 사용안함
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")
print("파이썬")

for i in range(10):
    print("파이썬")
    
print("파이썬" * 256)

num1 = 10
num2 = '20'

print(num1+num2)