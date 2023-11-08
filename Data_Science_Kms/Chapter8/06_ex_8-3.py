'''
작성 : 2023년 11월 8일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 심화문제 8-3
       3명의 학생의 학번, 이름, 전화번호의 3쌍의 요소를 가지는 student_tuple이라는 튜플이 존재한자.

       이 튜플을 수정하여 {학번: [이름, 전화번호]}의 쌍으로 이루어진 딕셔너릴 만들어 출력
       반복문 활용

       이 정보를 이용하여 학생의 학번을 입력받아
       이름과 전화번호를 출력하는 학사정보 프로그램 작성

       student_tuple의 마직막 항목으로 학점을 추가한다.
       이 정보를 바탕으로 딕셔너리를 만들어 출력

       학생의 학점 평균을 출력
'''
# 튜플 생성
student_tuple = [('202395001', '홍일동', '010-1234-1234'),
                 ('203395002', '홍이동', '010-4321-4321'),
                 ('202395003', '홍삼동', '010-1010-1010')]

# 빈 딕셔너리 생성
result_dict = {}
for id_num, name, phone_num in student_tuple:
    result_dict[id_num] = [name, phone_num]

# 딕셔너리 출력
for key, value in result_dict.items():
    print(key, ":", value)

# 학생의 학번을 입력받아 정보 검색 및 출력
account = input("학번을 입력하시오: ")

if account in result_dict:
    student_info = result_dict[account]
    print("학번:", account)
    print("이름:", student_info[0])
    print("전화번호:", student_info[1])
else:
    print("해당 학번의 정보를 찾을 수 없습니다.")

# 학점을 추가한 튜플
result_dict['202395001'].append(4.5)
result_dict['203395002'].append(3.8)
result_dict['202395003'].append(3.5)

for key, value in result_dict.items():
    print(key, ":", value)

# 학생의 학점 평균을 출력
print("전체 학생 평균 학점")
sum = 0
for key, value in result_dict.items():
    sum += value[2]

print(f"평균 : {sum/3:.2f}")














'''
Chatgpt쓰면 좇같이 알려준다.
# 학점을 추가한 튜플 생성
student_tuple_append_grades = [('202395001', '홍일동', '010-1234-1234', '4.5'),
                             ('203395002', '홍이동', '010-4321-4321', '3.9'),
                             ('202395003', '홍삼동', '010-1010-1010', '2.8')]

# 빈 딕셔너리 생성
result_dict_append_grades = {}
for id_num, name, phoen_num, grades in student_tuple_append_grades:
    result_dict_append_grades[id_num] = {'이름': name, '전화번호': phoen_num, '학점': grades}

# 딕셔너리 출력
for key, value in result_dict_append_grades.items():
    print(key, ":", value)

# 학점 평균 계산
grades = [student[3] for student in student_tuple_append_grades]
average_grade = sum(ord(grade) - ord('A') for grade in grades) / len(grades)
print("학점 평균:", average_grade)
'''