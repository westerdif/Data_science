'''
작성 : 2023년 11월 8일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 키와 값을 가지는 딕셔너리
'''
#비교연산자
num1 = {1,2,3}
num2 = {1,2,3}

#결과출력
print(f"num1 == num2 : {num1 == num2}")

# 6개의 숫자로 집합생성
num_set = {2,4,6,6,7,9}

#결과출력
print(f"num_Set : {num_set}")
print(f"num_Set의 길이 : ", len(num_set))
print(f"num_Set의 최대값 : ", max(num_set))
print(f"num_Set의 최소값 : ", min(num_set))
print(f"num_Set의 합 : ", sum(num_set))

print("======================")


num1 = {1,2,3}
num2 = {3,4,5}

#합집합
print(num1 | num2)

#합집합 메소드
print(num1.union(num2))

# 교집합 및 메소드
print(num1 & num2)
print(num1.intersection(num2))

# 차집합 및 메소드
print(num1 - num2)
print(num1.difference(num2))

# 대칭 차집합 및 메소드
print(num1 ^ num2)
print(num1.symmetric_difference(num2))