'''
작성일 : 2023년 10월 4일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 
'''
#단어를 입력
test = input('단어를 입력하세요 : ')

print(":::break1:::")
#반복문 설정
for i in test:
    #만약 a,e,i,o,u 라면
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        #종료
        break
    #아니면
    else:
        #결과 출력
        print(i, end = '')
        
print()
print(":::break2:::")
for i in test:
    #만약 a,e,i,o,u 라면
    if i in ['a', 'i', 'e', 'o', 'u', 'A', 'I', 'E', 'O', 'U']:
        #종료
        break
    #아니면
    else:
        #결과 출력
        print(i, end = '')
        
print()
print(":::continue:::")
for i in test:
    #만약 a,e,i,o,u 라면
    if i in ['a', 'i', 'e', 'o', 'u', 'A', 'I', 'E', 'O', 'U']:
        #처음부터 다시 반복
        continue
    #결과 출력
    print(i, end = '')