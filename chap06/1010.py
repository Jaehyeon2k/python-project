import numpy as np

# p38 넘파이 배열 합치기
arr1 = np.arange(8).reshape(2, 4)
arr2 = np.arange(8, 16).reshape(2, 4)
print(arr1)
print(arr2)
print(np.concatenate((arr1, arr2), axis=0))
print(np.concatenate((arr1, arr2), axis=1))

# p39 넘파이 배열 분리
arr = np.arange(8).reshape(2, 4)
print(arr)

up, down = np.split(arr, 2, axis=0)
print(up)
print(down)

left, right = np.split(arr, 2, axis=1)
print(left)
print(right)