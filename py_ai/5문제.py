import numpy as np

'''
병원에서는 실험 대상자들의 체질량 지수(BMI: Body Mass Index)를 계산하고
싶다고 하자.
heights = [ 1.83, 1.76, 1.69, 1. 86, 1.77, 1.73 ]
weights = [ 86, 74, 59, 95, 80, 68 ]

BMI = weights/(height)*2
'''


heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73 ]
weights = [ 86, 74, 59, 95, 80, 68 ]

arr_height = np.array(heights)
arr_weight = np.array(weights)

arr_bmi = arr_weight/(arr_height**2)
print(arr_bmi)