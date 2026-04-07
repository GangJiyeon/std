'''사용자로부터 정수(빨간색)를 입력 받아서 for문을 이용하여서 팩토리얼을
계산해보자.'''

num = int(input("정수를 입력하시오: "))

total = 1
for x in range(num, 1-1, -1):
    total *= x


print(total)