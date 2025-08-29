# ------------------------ 타입 확인

# message = 'hello'
# value = 10
# result = value + 10
# checked = True
# print(result)
# print(type(checked))
# print(value, message)

# ----------------------------------------------- 형변환

# strValue = '1'
# value2 =  int(strValue)
# print(type(value2), type(strValue))

# value3 = 2
# str2 = str(value3)
# print(type(str2), type(value3))

# value1 = 1
# value2 = 1
# value3 = value1 + value2
# print(value3)

# str1 = "1"
# str2 = "1"
# str3 = str1 + str2
# print(str3)

# ------------ 사용자로 부터 입력

# name = input()
# print("hello", name)

# 사용자로 부터 10을 입력받아 입력받은 값의 10을 더한 값

# try:
#   value = int(input())
#   print(value + 10)
# except Exception as e:
#   print(e)

# --------------- 조건식

# value1 = int(input())

# if value1 > 0:
#     print("positive")
# elif value1 < 0:
#     print("negative")
# else:
#     print("zero")

# print("bye")

# result1 = value1 % 2
# result2 = value1 % 3

# if (result1 == 0) and result2 == 0:
#     print('6의 배수')
# elif result1 == 0 or result2 == 0:
#     print("2의 배수 또는 3의 배수")

# # 삼항 연산자
# result = 'OK' if value1 > 5 else 'NG'
# print(result)

# # 범위 연산
# if 0 <= value1 <= 10: # 0 <= value and value <= 10 와 같다
#     print("valid")


# for 반복문 ----------
# for i in range (1, 10):
#     for j in range (2, 10):
#         print(j,"X",i, "=", j*i, end="\t")
#     print()


# --------while 반복문
# pw = input("비밀번호: ")

# while len(pw) < 8:
#     print("8글자 이상 입력하세요.")
#     pw = input("비밀번호: ")

# ----- 함수
def hello(name):
    return "hello ", name

result = hello("user")

print(result[0])
print(result[1])

def getArea(width = 0, height = 0):
    return width * height

area1 = getArea(100,100)
area2 = getArea(height=100, width=100)
area3 = getArea()