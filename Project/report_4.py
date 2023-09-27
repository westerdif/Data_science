'''
학과 : 컴퓨터공학부
학번 :
설명 : 파이이썬의 random.randit(1,100)을 이용하여 1에서 100 사이으 임의의 난수 2개를 생성해서. 그 다음에 두 수의 합을 묻는 질문을 사용자에게 던지도록 하자. 만일 사용자가 두 수의 합을 맞추면
       "참 잘했어요"를 출력, 만일 틀린다면 "정답은 000입니다.
'''
import random

# 1에서 100 사이의 난수 2개 생성
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# 두 수의 합 계산
correct_sum = num1 + num2

# 사용자에게 두 수의 합을 맞추도록 질문
user_guess = int(input(f"{num1} + {num2}의 합은 얼마일까요? "))

# 만약 정답이라면
    #참 잘했어요! 출력
if user_guess == correct_sum:
    print("참 잘했어요!")

#아니면
    #000입니다. 출력
else:
    print(f"정답은 {correct_sum}입니다.")


print("============================================")

import random

# 정답을 맞추는 함수
def guess_sum_game():
    # 정답을 생성
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_sum = num1 + num2

    # 시도 횟수 초기화
    attempts = 0

    print("두 수의 합을 맞추는 게임을 시작합니다.")

    while True:
        user_guess = int(input(f"{num1} + {num2}의 합을 맞춰보세요: "))
        attempts += 1

        if user_guess == correct_sum:
            print(f"정답입니다! {attempts}번 시도하여 맞췄습니다.")
            break
        elif user_guess < correct_sum:
            print("너무 작습니다. 다시 시도해보세요.")
        else:
            print("너무 큽니다. 다시 시도해보세요.")

# 게임 실행
guess_sum_game()
