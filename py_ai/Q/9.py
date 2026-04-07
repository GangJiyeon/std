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