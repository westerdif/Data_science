'''
작성 : 2023년 11월 8일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 파티 참석자
'''
# 파티 참석자 집합 생성
party1 = set(['Park', 'Kim', 'Lee'])
party2 = set(['Park', 'Choi'])

# 파티를 모두 참석한 사람 출력
print("2개의 파티에 모두 참석한 사람은  다음과 같습니다.")
print(party1.intersection(party2))

# 파티1, 파티2에 참석한 사람들 출력
print("파티1, 파티2에 참석한 사람들은 다음과 같습니다.")
print(party1.union(party2))

# 두개의 파티를 중복없이 참석한 사람 출력
print("두개의 파티를 중복없이 참석한 사람은  다음과 같습니다.")
print(party1.symmetric_difference(party2))

# 파티 1에만 참석한 사람 출력
print("파티 1에만 참석한 사람은  다음과 같습니다.")
print(party1.difference(party2))