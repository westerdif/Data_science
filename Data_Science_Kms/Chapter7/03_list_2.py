'''
작성일 : 2023년 10월 18일 
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 :  릿트에서 사용 가능한 함수
'''
#리스트 생성
num_list = [1,2,3,4,5,6,7,8,9]


print(f"num_list : {num_list}")
print(f"num_list 길이 :", len(num_list))  #리스트의 길이
print(f"num_list 최대값 :", max(num_list)) #리스트의 최대값
print(f"num_list 최소값 : ", min(num_list)) #리스트의 최소값
print(f"num_list 항목의 합계 :", sum(num_list)) #리스트의 합계
print(f"num_list 항목의 평균 :", sum(num_list)/len(num_list))
print(f"num_list 항목 중 0이 아닌 원소가 있나 :", any(num_list)) #0이 아닌 원소가 있는지 확이