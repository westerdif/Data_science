'''
작성일 : 2023년 9월 20일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 선택문 if
       설명 :   년도를 입력 받아 윤년인지 아닌지 판단하는 프로그램 작성
        조건:   1.기본적으로 연도를 4로 나누어떨어지면 윤년이다.
                2.그러나 100으로 나누어 떨어지지 않는 해는 윤년이다.
                3.그러나 400으로 나누어 떨어지는 해는 윤년이다.
'''
'''
#년도를 입력받는다.
year = int(input('년도를 입력하시오 : '))

#만약에 년도가 4로 나누어 떨어지면
if year % 4 == 0:
    #만약 년도가 100으로 나누어 떨어지면
    if year % 100 != 0:
        #만약 년도가 400으로 나누어 떨어지면
        if year % 400 == 0:
            print("{}년은 윤년입니다." .format(year))
        
        #아니면 
        #윤년이 아닙니다.
        else:
            print("윤년이 아닙니다.")    
    
    #아니면
    #{}년은 윤년입니다.
    else:
        print("{}년은 윤년입니다." .format(year))

#아니면
#윤년이 아닙니다.
else:
    print("윤년이 아닙니다.")
'''
#년도를 입력받는다.
year = int(input('년도를 입력하시오 : '))

#판단
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("윤년입니다.")

else:
    print(f"{year}년은 윤년이 아닙니다.")