# 함수 
'''
쓰는 이유
코드간결 > 가독성, 전체기능이해, 흐름파악, 관리 용이
재사용, 효율적
'''

# 함수종류
'''
1) 사용자 정의 함수: 
- 이름은 변수규칙이랑 같음
- 구조
def 함수명(매개변수, ...):
    stmt
    return
'''



def sing():
    print("노래를 불러요~~~")

def turn_off():
    print("불을 끄고!!")




# 게임을 만들자!
# 큰수 찾기 게임
def max1(num1, num2):
    if num1 < num2:
        return num2
    else:
      return num1



def game369(num):
    a = num //10
    b = num % 10

    if a==3 or a == 6 or a == 9:
        return "통과"
    elif b==3 or b==6 or b== 9:
        return "통과"
    else:
        return "띠용"

# 선언 이후에 호출해야 한다
turn_off()
sing()

num = int(input('숫자'))
print(game369(num))

print(max1(num, 35))



# 람다 함수
'''
람다표현식을 인수로 사용

람다매개변수=> 식
map(): 리스트 요소를 지정된 함수로 처리
'''

def plus_five(x):
    return x + 5

print(plus_five(6))

plus_five2 = lambda x: x+5

print(plus_five2(6))  

print(list(map(plus_five, [30, 20, 10])))


# 메소드: 객체안에 정의된 함수
name = "Harry Parter"
lower_name = name.lower() 
print(lower_name)
name = "Harry Parter"
new_name = name.replace("Parter", "Porter") 
print(new_name)


# 팩토리얼 계산 함수

input_number = int(input("정수를 입력하시오: "))


def fac(input_number):
    a = 1
    for x in range(input_number, 0, -1):
        a *= x
    return a

print(fac(input_number))