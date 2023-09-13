'''     
작성일 : 2023년 9월 13일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 평균시속과 이동시간을 입력받아
       이동 시간은 시,분,초 단위로 출력하고,
       이동한 거리를 계산하여 출력하시오.
'''
#평균시속과 이동시간을 입력받는다.
avg_time = float(input("평균시간을 입력하시오 : "))
mov_time = float(input("이동시간을 입력하시오 : "))

#이동거리를 구하는 공식
mov_km = avg_time * mov_time

#시, 분, 초로 바꾸는 식
total_seconds = mov_time * 3600  

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60


#평균시속과 이동시간 그리고 이동거리를 출력
print("평균시속은 {} Km/h" .format(avg_time))
print("{:.0f} 시간 {:.0f} 분 {:.0f} 초" .format(hours,minutes,seconds))
print("이동거리는 {} Km" .format(mov_km))