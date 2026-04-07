'''
정수들이 저장된 리스트에서 두 번째로 큰 수를 찾아보자.
number_list = -7, 2, 3, 8, 6, 6
'''
number_list = [-7, 2, 3, 8, 6, 6]

number_list.sort()
print(number_list)
num = number_list[-2:-2-1:-1]

print(num, number_list[-2])