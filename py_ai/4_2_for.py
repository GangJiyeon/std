# for문 형태
'''
for 제어변수 in 범위가있는것:
    내용

* 범위가 있는 것(여러개)
'문자열'
리스트 = []
range(시작값, 종료값+1, 증가값)
'''

for a in range(5):
    print(a, end=' ')

odd = [1, 3, 5]
for a in odd:
    print(a, end='')

for a in '살려주세요':
    print(a, end='')

print()

# for문 중첩

print(f"우리 가게 메뉴 ====")

base = ['양상추', '양배추']
main = ['새우', '닭가슴살']
sauce = ['오리엔탈', '발사믹']

i = 1
for b in base:
    for m in main:
        for s in sauce:
            print(f"메뉴 i: {s} 소스를 뿌린 {m} {b} 샐러드")


num1 = int(input("정수를 입력하시오: "))
answer = 1

for x in range(num1, 0, -1):
    answer *= x

print(f"{num1}! 은 {answer}")



# 파이 계산하기 - 이건 내생각
Pi = 0

play = int(input("반복횟수: "))
plus = True
for i in range(1, 2*play, 2):

    if(plus):
        Pi += 4/i
        plus = False
    else:
        Pi -= 4/i
        plus = True


print(f"Pi = {Pi}")


# 
pi = 0

play = int(input("반복횟수: "))

for n in range(play):
    pi += ((-1) ** n) * (4 / (2*n + 1))

print(f"Pi = {pi}")