'''
작성 : 2023년 11월 8일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 집합 set()

        set()은 중복을 허용하지 않는다.
'''
# 빈 집합 생성
number = set()

# 숫자 3개로 이루어진 집합
number1 = {2,1,3} #딕셔너리를 생성할 떄 key값이 없다면 집합이다.
print(f"집합 : {number1}")

# 리스트로부터 집합 생성.
number2 = set([1,2,3,2,1])
print(f"집합 : {number2}") # 중복을 허용하지 않는다.

# 문자열을 집합으로 생성.
text1 = set("asdfasdf")
print(f"text1 : {text1}")

numbers = {2,4,5,1,2}
if 1 in numbers : # 집합 안에 1이 포함되어 있는가?
    print("집합에 1이 포함되어 있습니다.")

# 집합은 순서가 없어서 index()로 접근이 불가능하다.
# 반복문으로 접근하여 출력 가능하다.
numbers = {9,1,5,2,4,7,6,3,4,9,1}
for num in numbers :
    print(num, end='  ')

print()
print("=====================================")

#정렬 후 출력하기
for num in sorted(numbers) :
    print(num, end='  ')

print()
print("=====================================")

# 추가하기
numbers.add(100)
print(numbers)
for num in numbers :
    print(num, end='  ')

print()
print("=====================================")

# 삭제하기
numbers.remove(100)
print(numbers)
