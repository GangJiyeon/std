# while
'''
중단하고 나가기: break
건너뛰기: continue
아무것도 실행하지 않고 그냥 넘어감: pass
'''

age = int(input('나이를 입력하세요 ㅎㅎ: '))

i = 1
while age <= 50:
    
    if i == 1:
        print(f"올해 내 나이는 {age}")
    print(f"{i}년 뒤 내 나이는 {age}")
    age +=1
    i +=1

    stop = input("나이 카운트를 멈추고 싶으면 y")

    if stop == 'y':
        break

print("나이 카운트 종료!")


# 1에서 30사이 정수 중 7 배수 출력
list_of_7 = []
for x in range(1, 31):
    if x % 7 == 0:
        list_of_7.append(x)
    elif x % 2 == 0:
        continue
    else:
        pass

print(f"7의 배수: {list_of_7}")

# continue, pass 차이
for i in range(5):
    if i == 2:
        continue    # 해당 범위 for문을 냅다 종료하고 나가는 느낌
    print(i)
print("finish")

for i in range(5):
    if i == 2:
        pass        # 아무것도 입력되지 않은 듯한 느낌
    print(i)
print("finish")


# 중첩 반복문! 구구단을 만들자!!

while True:
    num = int(input("단 입력: (0누르면 종료)"))
    
    if num == 0:
        break

    a = 1
    while a <= 9:
        print(f"{num} * {a} = {num*a}")
        a += 1