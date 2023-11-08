'''
작성 : 2023년 11월 8일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 심화문제 8-6
       튜플을 가지는 student_tuple 리스트
       그 리스트는 학번, 이름, 전화번호로 이루어져 있다.

       리스트를 이용하여 {학번:이름}을 만들어 출력

       위에 딕셔너리를 이용하여 학번으로 조회를 할 경우 학번, 이름 과 전화번호가 출력 되도록 해라
'''
#리스트 생성
student_tuple = [('202395001', '홍일동', '010-1234-1234'),
                 ('203395002', '홍이동', '010-4321-4321'),
                 ('202395003', '홍삼동', '010-1010-1010')]

# 빈 딕셔너리 생성
result_dict = {}
for id_num, name, phone_num in student_tuple:
    result_dict[id_num] = [name, phone_num]

# 딕셔너리 출력
for key, value in result_dict.items():
    print(key, ":", value[0])

# 학생의 학번을 입력받아 정보 검색 및 출력
account = input("학번을 입력하시오: ")

if account in result_dict:
    student_info = result_dict[account]
    print(f"학번이 {account}인 학생은 {student_info[0]}이며 전화번호는 {student_info[1]}입니다.")
else:
    print("해당 학번의 정보를 찾을 수 없습니다.")