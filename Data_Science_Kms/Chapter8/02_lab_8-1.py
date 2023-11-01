'''
작성 : 2023년 11월 1일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : lab 8-1 편의점 재고 관리 프로그램
'''
#재고 딕셔너리 생성
items = {'커피음료' : 7, '펜' : 3, '종이컵' : 2, '우유' : 1, '콜라' : 4, '책' : 5}

#물건의 목록을 출력한다.
for key in items.keys():
    print(key, end=',')
print()

#물건의 이름을 입력받아 재고를 출력한다.
name  = input("물건의 이름을 입력하시오 : ")
print("재고 :", items[name])

print("============================")

# 재고 딕셔너리 생성
items = {'커피음료': 7, '펜': 3, '종이컵': 2, '우유': 1, '콜라': 4, '책': 5}

def check_stock():
    name = input("물건의 이름을 입력하시오 (끝을 입력하면 종료): ")
    return name

while True:
    print("물건 목록:")
    for item in items:
        print(item)
    
    name = check_stock()
    
    if name == '끝':
        break
    
    stock = items.get(name)
    if stock is not None:
        print(f"{name}의 재고: {stock}")
    else:
        print("해당 물건은 재고에 없습니다.")
        break
