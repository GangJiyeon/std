'''
물건 값의 7.5%가 부가세라고 하자. 물건값이 12345원일 때, 부가세를 소수점
2번째 자리까지 계산하는 프로그램
'''

price = 12345
tax_rate = 0.075

tax = price * tax_rate

print(f"부가세는 {tax:.2f} 입니다")




'''1626년에 아메리카 인디언들이 뉴욕의 맨하탄섬을 단돈 60길더(약 24달러)에
탐험가 Peter에게 팔았다고 한다. 382년 정도 경과한 맨하탄 땅값은 약 600억
달러라고 한다.
하지만 만약 인디언이 24달러를 은행의 정기예금에 입금 해두었다면 어떻게
되었을까? 예금 금리는 복리로 6%라고 가정하자. 그리고 382년이 지난 후에
는 원리금을 계산하여 보자.'''

money = 24
years = 382
interest = 0.06

final_value = money * ((1 + interest)**years)

print(f"원리금은 {final_value:.2f} 입니다")




name = input("안녕하세요! 저는 당신의 친구 ai에요. 제게 이름을 지어주세요")

print("우와! 저는 %s이군요" % name)
print("{}: 반가워요! ".format(name))

user_name = input("그럼 당신의 이름은 무엇인가요?: ")

print("{1}: {0}님 안녕하세요!".format(user_name, name))

print(f"{name}: {user_name}님, 무엇을 도와드릴까요?", end=' ')

print(f"대화를 원하면 1, 그외의 것은 2를 입력")

option = input("입력: ")