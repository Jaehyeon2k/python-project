import matplotlib.pyplot as plt
import numpy as np
import math


# # p8 선 그래프
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]

# # 선 그래프, x축 years값, y축 gdp값
# plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# # 제목 설정
# plt.title("GDP per capita")

# # y축 레이블 설정
# plt.ylabel("dollars")
# # png 이미지로 저장
# plt.savefig("gdp_per_capita.png", dpi=600)
# plt.show()

# # p9 난수 그래프
# x = [x for x in range(1000)]
# y = np.random.rand(1000) * 6 - 3

# plt.figure(figsize=(12, 4))
# plt.title("Random Numbers")
# plt.plot(x, y, "bo-")
# plt.axis((0, 1000, -3.5, 3.5))

# plt.show()

# # p10 범례(legend)
# x = [x for x in range(20)]          # x = 0 ~ 20 까지 정수 생성
# y = [x ** 2 for x in range(20)]     # y = x의 제곱값
# z = [x ** 3 for x in range(20)]     # z = x의 세제곱값

# plt.plot(x,x, label="linear")       # 각 선에 대한 레이블 지정
# plt.plot(x,y, label="quadratic")
# plt.plot(x,z, label="qubic")

# plt.xlabel("x label")               # x축 레이블
# plt.ylabel("y label")               # y축 레이블
# plt.legend()                        # 범례 표시
# plt.show()

# # p11 실습.사인 그래프
# x = []
# y = []

# for angle in range(360):
#     x.append(angle)
#     y.append(math.sin(math.radians(angle)))

# plt.plot(x,y)
# plt.title("Sine Wave")
# plt.show()

# # p12 막대 그래프
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]

# plt.bar(range(len(years)), gdp)

# plt.title("GDP per capita income")
# plt.ylabel("dollars")

# plt.xticks(range(len(years)), years)
# plt.show()

# # p13 다중 막대 그래프
# years = [1965, 1975, 1985, 1995, 2005, 2015]
# ko = [130, 650, 2450, 11600, 17790, 27250]
# jp = [890, 5120, 11500, 42130, 40560, 38780]
# ch = [100, 200, 290, 540, 1760, 7940]

# x = np.arange(len(years))
# plt.bar(x - 0.25, ko, width = 0.25, label='Korea')
# plt.bar(x + 0.0 , jp, width = 0.25, label='Japan')
# plt.bar(x + 0.25, ch, width = 0.25, label='China')

# plt.plot(ko)
# plt.plot(jp)
# plt.plot(ch)

# plt.xticks(x, years)
# plt.legend()
# plt.show()

# # p14 산포도(산점도) 그래프
# x = np.arange(20, 50)
# y = x + 2*np.random.randn(30)

# plt.scatter(x, y)
# plt.title("Real Age vs Physical Age")
# plt.xlabel("Real Age")
# plt.ylabel("Physical Age")

# plt.savefig("kkk.png", dpi=600)
# plt.show()

# # p15 산포도(산점도):색상, 크기 지정
# np.random.seed(0)
# n = 50

# x = np.random.rand(n)
# y = np.random.rand(n)
# area = (30 * np.random.rand(n))**2
# colors = np.random.rand(n)

# plt.scatter(x,y, s=area, c=colors)
# plt.show()

# # p16 파이 차트
# ratio = [34, 32, 16, 18]
# labels = ['Apple', 'Banana', 'Melon', 'Grape']
# plt.pie(ratio, labels=labels, autopct='%1.1f%%')
# plt.show()

# p17 파이 차트: 부채꼴 분리
ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grape']
explode = (0, 0.10, 0, 0.10)  # 첫 번째 조각만 분리
plt.pie(ratio, labels=labels, autopct='%1.1f%%', startangle=260, counterclock=False, explode=explode)
plt.show()

# p19 히스토그램

weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
 80, 59, 67, 81, 69, 73, 69, 74, 70, 65]
plt.hist(weight, bins=25)
plt.show()

# p23 까지함