'''
작성 : 2023년 11월 1일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 키와 값을 가지는 딕셔너리
'''
#빈 딕셔너리 생성
phone_book1 = {}

#딕셔너리에 값 저장. key, value
phone_book1['구민수'] = '010-1111-2222'

print(f"'phone_book1 : {phone_book1}") #{'구민수': '010-1111-2222}

#딕셔너리에 값 저장. 2.{key:value}
phone_book2 = {'구민수' : '010-2472-2472', '홍길동' : '010-3535-2222'}
print(f"phone_book2 : {phone_book2}")

phone_book3 = {}
phone_book3['구민수'] = '010-2121-3596'
phone_book3['홍길동'] = '010-1851-3596'
phone_book3['장성우'] = '010-2891-3596'
phone_book3['이근우'] = '010-5921-3596'
phone_book3['이휘'] = '010-4569-3596'

print()
print("::전화번호 phone_Book3 출력::")
#모든 key 출력
print(phone_book3.keys())
#모든 value 출력
print(phone_book3.values())
#모든 key와 value 출력
print(phone_book3.items())

print()
print("::전화번호 phone_book3.items() 출력::")
for name, phoen_number in phone_book3.items() :
    print(name, ':', phoen_number)


print()
print("::전화번호 phone_book3[keys]로 접근하여 출력::")
for key in phone_book3.keys() :
    print(key, ":", phone_book3[key])


print()

print("딕셔너리 작성 시 : (:)을 기준으로 key:value 작성")
peron_dict = {'name' : '구민수', 'age' : 19, 'class' : '1학년'}

print('name :', peron_dict['name']) #딕셔너리의 'name'을 키로 값을 조회하여 출력
print('age :', peron_dict['age'])
print('class :', peron_dict['class'])

print()

print("::정렬::")
#phone_book3 정렬
#딕셔너리 키를 기준으로 정렬하여 리스트로 반환.
print(sorted(phone_book3))


#lamda 함수 => 이름이 없는 함수. 변수 생성 금지 == lamda x(매개변수) : x+y(반환 값)
print(":: 키를 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x: x[0]) 
print(sort_phone_book3)
print("====================")
print(":: 값을 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x: x[1])
print(sort_phone_book3)


print()

print("::항목 삭제")
del phone_book3['구민수']
print(phone_book3)

print("::전체 삭제")
phone_book3.clear()
print(phone_book3)