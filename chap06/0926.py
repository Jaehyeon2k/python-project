import numpy as np

arr = [1, 2, 3, 4]
print(arr)
np_arr = np.array(arr)
print(np_arr)

# p16 배열 인덱싱과 슬라이싱
arr = np.array([1, 2, 3, 4, 5])
n = arr.size

print(arr[0])
print(arr[-1], arr[n-1])

print(arr[1:4])
print(arr[0:-1], arr[0:4])
print(arr[:], arr[0:], arr[:n],arr[0:n])

# 논리 인덱싱
arr = np.array([1, 2, 3, 4, 5])
condition = arr % 2 == 0
print(condition)
even_arr = arr[condition]
print(even_arr)

arr = np.array([50, 60, 70, 80, 90])
condition = arr >= 80
print(condition)
pass_arr = arr[condition]
print(pass_arr.size)

arr = np.array(["김제로", "김하나", "이둘", " 이하나", "이제로"])
result = np.strings.find(arr, "김")
print(result)
result_arr = arr[result >= 0]
print(result_arr)

# p21 2차원 배열 논리 인덱싱
arr = np.array([[1, 2, 3], [4, 5, 6]])

larr = arr % 2 == 0
print(larr)

print(arr[larr])

arr1 = np.array([1, 2, 3, 4])
condition = np.array([True, False, True, False])
print(arr1[condition])

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
condition = np.array([False, True])
print(arr2[condition])

# p23 2차원 배열에서 조건 만족 행 추출
lst = [[177, 77.1],
       [183, 80.1],
       [185, 78.3],
       [173, 80.3],]
arr = np.array(lst)

condition = arr[:, 1] >= 80
print(condition)
print(arr[condition])

# print("몸무게가 80 이상")
# print(arr[arr[:, 1] >= 80])

# print("키가 180 이상")
# print(arr[arr[:, 0] >= 180])

# p25 넘파이 배열 생성/초기화 함수
print(np.zeros((3, 4))) # 3행 4열 0으로 초기화

print(np.ones((3, 4))) # 3행 4열 1로 초기화

print(np.eye(3)) # 3행 3열 단위행렬

#p26 넘파이 배열 생성 함수 : arange()

# 크기 10인 배열 생성, 0~9로 초기화
print(np.arange(10), np.array(range(10)))
# 크기 9인 배열 생성, 1~9로 초기화
print(np.arange(1, 10), np.array(range(1, 10)))
# 크기 5인 배열 생성, 0~8까지 2씩 증가
print(np.arange(0, 10, 2), np.array(range(0, 10, 2)))

# p 29 넘파이 배열 형태 변경

arr1 = np.arange(8)
print(arr1, "\n")

arr2 = arr1.reshape(2, 4)
print(arr2, "\n")

print(arr2.flatten(), arr2.reshape(-1))

# p31 난수 배열 생성
np.random.seed(1)
arr1 = np.random.rand(10)
print(10*arr1 + 10)

arr2 = np.random.randint(1, 11, size=(3, 5))
print(arr2)

print(np.random.randint(1, 6, size=10))

# p33 정규 분포 난수 생성

np.random.seed(1)
print(np.random.normal(0, 1, 5))

np.random.seed(1)
print(np.random.random(5))
print()

np.random.seed(1)
print(np.random.normal(10,2, (2, 5)))
print()

np.random.seed(1)
print(np.random.randn(2, 5) * 2 + 10)

# p35 난수 관련 함수

np.random.seed(None)
x = np.arange(1, 11)
np.random.shuffle(x)
print(x)

y = np.arange(1, 11)
print(np.random.permutation(y))
print(y)

fruits = ["apple", "banana", "cherries", "durian", "grapes", "lemon", "mango"]
pb = [0.1, 0, 0.2, 0.5, 0.1, 0.05, 0.05]
print(np.random.choice(fruits, 3, replace=False, p=pb))

# p37 넘파이 배열 평균 계산

arr = np.array([[99, 93, 60], [98, 82,93], [93, 65, 81], [78, 82, 81]])
print(arr, "\n")

print(np.mean(arr, axis=0)) # 열 방향 평균
print(arr.mean(axis=0), "\n")

print(np.mean(arr, axis=1)) # 행 방향 평균
print(arr.mean(axis=1), "\n")
