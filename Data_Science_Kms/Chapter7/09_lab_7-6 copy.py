'''
작성일 : 2023년 11월 1일 
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 :  lab 7-6 도시의 이름과 인구를 튜플로 묶어보자
'''
#주어진 도시 정보 리스트
city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 9765), ('대전', 9765)]

#초기화
#최대 인구수
max_population = city_info[0][1]  #첫 번쪠 항목이 기준.
#최소 인구수를 무한대 값으로 초기화
min_population = city_info[0][1]  
#전체 인구수의 합
total_population = 0  


#최대 인구를 가진 도시
max_city = city_info[0][0] #첫 번쪠 항목이 기준.
#최소 인구를 가진 도시
min_city = city_info[0][0] 

for city, population in city_info: #도시명과 인구 수를 각각 변수에 저장
    #각 도시의 인구를 전체 인구에 더함
    total_population += population  
    if population > max_population:
        #최대 인구수 갱신
        max_population = population
        #최대 인구를 가진 도시 업데이트
        max_city = city 

    if population < min_population:
        #최소 인구수 갱신
        min_population = population 
        #최소 인구를 가진 도시 업데이트
        min_city = city  

#결과 출력
print(f"최대 인구: {max_city}, 인구: {max_population}천명")
print(f"최소 인구: {min_city[0]}, 인구: {min_population}천명")
print(f"리스트 도시 평균 인구: {total_population / len(city_info)}천명")
