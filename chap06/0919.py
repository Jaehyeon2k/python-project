# p8 넘파이 배열 생성
import numpy as np
arr = np.array([1, 2, 3])
print(arr)
print(type(arr))

# p10 넘파이 배열의 속성(필드)
arr1 = np.array([1, 2, 3])
print(arr1)
print(arr1.ndim, arr1.shape, arr1.dtype, arr1.itemsize, arr1.size)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(arr2.ndim, arr2.shape, arr2.dtype, arr2.itemsize, arr2.size)

arr3 = np.array([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
print(arr3)
print(arr3.ndim, arr3.shape, arr3.dtype, arr3.itemsize, arr3.size)

# p12 리시트와 넘파이 배열 + 연산의 차이
lst1 = [1, 2, 3] 
lst2 = [4, 5, 6]
print(lst1 + lst2) # 리스트 + 리스트 ==> 리스트 연결 연산자

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2) # 넘파이 배열 + 연산자 ==> 원소별 덧셈 연산

# p13 넘파이 배열 곱셈 연산자 : *와 @
arr1 = np.array([[1, 1], [2, 2]])
arr2 = np.array([[1, 2], [3, 4]])

arr3 = arr1 * arr2 # 넘파이 배열 * 연산자 => 원소별 곱셈
print(arr3)

arr4 = arr1 @ arr2 # 넘파이 배열 @ 연산자 => 행렬 곱셈
print(arr4)

# p14 실습.BMI 계산
h = [1.83, 1.75, 1.71, 1.85, 1.77, 1.73]
w = [80, 74, 59, 90, 77, 78]

harr = np.array(h)
warr = np.array(w)

bmi = warr / harr**2
print(bmi)
