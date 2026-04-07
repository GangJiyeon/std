'''
0부터 99까지의 정수 중에서 2의 배수이고 동시에 3의 배수인 수들을 모아서
리스트로 만들어보자.
'''
list_3 = []

list_3 = [x for x in range(0, 99+1, 1) if x % 2 == 0 and x % 3 ==0]
print(list_3)

list_4 = []

for x in range(0, 99+1, 1):
    if x % 6 ==0:
        list_4.append(x)


print(list_4)