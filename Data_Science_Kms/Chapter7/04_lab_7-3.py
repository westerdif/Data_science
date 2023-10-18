'''
작성일 : 2023년 10월 18일 
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 :  도시의 인구 자료에 대한 슬라이싱하기.
'''
# 인구 리스트 생성
popula = ['seoul', 9765, 'busan', 3441, 'incheon', 2954]

# 서울 인구인 두 번째 요소를 출력
seoul_population = popula[1]
print("서울 인구:", seoul_population)

# 마지막 요소인 인천의 인구를 출력 (음수 인덱스 사용)
incheon_population = popula[-1]
print("인천 인구:", incheon_population)

# 각 도시의 인구를 step(2씩) 값을 이용하여 출력
cities = popula[::2]  # 2씩 증가하는 슬라이싱
print("도시 리스트:", cities)

# 각 도시의 인구를 step(2씩) 값을 이용하여 출력한 후 이 값들의 합을 출력
populations = popula[1::2]  # 2씩 증가하는 슬라이싱, 인구만 가져오기
total_population = sum(populations)
print("도시별 인구:", populations)
print("전체 인구 합계:", total_population)
