'''
작성 : 2023년 11월 15일
학과 : 컴퓨터공학부
학번 : 202395001
이름 : 구민수
설명 : 
'''
text = "There's a reason some people are working to make it harder to vote,\
        especially for people of color.\
        It's because when we show up, things change."

# 뛰어쓰기를 기준으로 문자열을 분리하고, 단어의 개수를 찾아라
print(text.split())
text1 = text.split()
print(len(text1))

print()

print("==================================================================")
# 도전문제 9-1
# 회사 이름은 **로 표시
# KT, Samsung, LG, SKT
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
        Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
        U+ Mystic Pink 30%, SKT Mystic Blue not disclosed)'

# 회사명을 **로 바꾸기
text1 = text.replace('KT', '**').replace('LG', '**').replace('SKT', '**').replace('Samsung', '**')

print("원본:")
print(text)
print()
print("변경된 텍스트:")
print(text1)

# 모든 문자를 소문자로 변환
text_lower = text.lower()

# 소문자로 바뀐 단어들을 공백으로 구분한다.
words = text_lower.split()

# 구분된 단어를 검사한다. (판단) => 단어가 KT 또는 Samsung 또는 LG 또는 SKT인가?
# 검사하는 단어가 회사명이면 **로 바꾸어 리스트에 저장
replace = ['kt', 'lg', 'skt', 'samsung']
for i in range(len(words)):
    if words[i] in replace:
        words[i] = '**'

# 분리된 단어들을 합친다.
text2 = ' '.join(words)

print("\n소문자로 바뀐 단어와 회사명이 대체된 텍스트:")
print(text2)


print("====================================================")
