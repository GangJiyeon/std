'''사용자료부터 정수(빨간색)를 입력 받아서 def문을 이용하여 팩토리얼을
계산해보자.'''

def factorial1(a):
    total = 1
    for x in range(a, 1-1, -1):
        total *= x

    return total

print(factorial1(int(input("정수: "))))