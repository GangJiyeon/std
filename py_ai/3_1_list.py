list1 = [1, 2, 3, 4, 5, 6, [7, 8], 'hi']


print(f"list1           = {list1}")
print(f"list1[::]       = {list1[::]}")
print(f"list1[0::1]     = {list1[0::1]}")
print(f"list1[0:6+1:3]     = {list1[0:6+1:3]}")
print(f"list1[-1:-9:-1]     = {list1[-1:-9:-1]}")
print(f"list1[6][1]     = {list1[6][1]}")

list1[1:3+1:2] = [1, 1]

print(f"{list1}")


my_list = []

print(f"my list: {my_list}")

my_list.append(1)
print(f"my list에 1추가하기: {my_list}")

my_list.insert(1, 2)
print(f"my list의 1번 인덱스에 2추가하기: {my_list}")

my_list.reverse()
print(f"my list 내림차순정렬: {my_list}")

my_list.sort()
print(f"my list 오름차순정렬: {my_list}")


'''
numbers = [1,2,3,4,5,6,7,8,9,10]
1. 위의 리스트에 대하여, 리스트 슬라이싱 만을 이용하여 리스트의 요소
들의 순서를 거꾸로 하면서 두 개씩 건너뛰어 보자. 결과는 아래와 같이
만드시오.
[10, 8, 6, 4, 2]

2. 리스트 슬라이싱 만을 이용하여 아래와 같이 첫 번째 요소만을 남기고
전부 삭제하시오.
'''
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[-1::-2])

numbers = numbers[0]
print(numbers)


'''
정수들이 저장된 리스트에서 두 번째로 큰 수를 찾아보자.
number_list = -7, 2, 3, 8, 6, 6
'''
number_list = [-7, 2, 3, 8, 6, 6]

number_list.sort()
print(number_list)
num = number_list[-2:-2-1:-1]

print(num, number_list[-2])


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