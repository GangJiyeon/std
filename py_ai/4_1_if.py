# 선택문

# 1. 회원이면 '어세오세요', 아니면 '회원가입 해주세요'
member = input('회원이십니까? (y/n)')
if member == 'y':
    print('어서오세요')
else:
    print('회원가입 해주세요')


# 2. 입력받은 나이에 따라 놀이동산 입장료 출력
age = int(input('나이를 입력해주세요(숫자만): '))
if age == 0:
    age = int(input('0이 아닌 나이를 입력해주세요(숫자만): '))
price = 20000

if 1 <= age and age < 6:
    price = 0
elif age >= 60:
    price *= 0.5

print(f"입장료는 {price} 입니다.")


# 3. 산술 퀴즈 프로그램 - 정수입력 홀짝 판단
user_num = int(input("정수를 입력하시오: "))

if user_num % 2 == 0:
    print("짝수")
else:
    print("홀수")


# 배송비 계산 프로그램 
'''
국가, 가격 입력 받기

한국
가격이 2만원 이상, 배송비 무료
아니면 3000원

미국
10만원 이상, 배송비 무료
아니면 8000
'''

nation = input("국가: ")
price = int(input("가격: "))
fee = 0

if nation == "us":
    if price < 100000:
        fee = 8000
else:
    if price < 20000:
        fee = 3000

print(f"배송비는 {fee}")