'''
작성일 : 2023년 10월 11일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 여러개의 값을 넘겨주고 여러개의 값을 돌려받기
       
       
       두 수를 전달하여 사치 연산의 결과값을 돌려준다.
       
       [알고리즘]
       (함수)
        입력받은 두 수를 매개변수에 저장
        입력받은 두 수를 가지고 사칙연사을 계산하다.
            #만약 opt = 1이면 더한다.
            #opt = 2이면 뺀다
            #opt = 3이면 곱한다.
            #opt = 4이면 나눈다.
            #opt = 5이면 나머지를 구한다.
       
       (메인)
        두 수를 입력받는다.
        함수호출
        호출받은 값을 출력
'''
def cals(num1, num2):
    sum = num1 + num2
    minus = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    rest = num1 % num2
    
    return sum, minus, mul, div, rest

num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

sum, minus, mul, div, rest = cals(num1, num2)

print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {minus}")
print(f"{num1} * {num2} = {mul}")
print(f"{num1} / {num2} = {div}")
print(f"{num1} % {num2} = {rest}")  


print("=====================================")

def cals(num1, num2, opt):
    if opt == 1:
        result = num1 + num2
    elif opt == 2:
        result = num1 - num2
    elif opt == 3:
        result = num1 * num2
    elif opt == 4:
        result = num1 / num2
    elif opt == 5:
        result = num1 % num2
    else:
        result = None

    return result

num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))
opt = int(input("연산을 선택하세요 (1: 덧셈, 2: 뺄셈, 3: 곱셈, 4: 나눗셈, 5: 나머지): "))

result = cals(num1, num2, opt)

if result is not None:
    operator = '+' if opt == 1 else '-' if opt == 2 else '*' if opt == 3 else '/' if opt == 4 else '%'
    print(f"{num1} {operator} {num2} = {result}")
else:
    print("유효하지 않은 옵션을 선택했습니다.")
