# import requests
# from bs4 import BeautifulSoup

# ----------- 당근마켓 크롤링
# page = requests.get("https://www.daangn.com/hot_articles")
# soup = BeautifulSoup(page.content, "html.parser")

# # print(soup.h2)
# # print("-------------------------------")
# # print(soup.h1.string)
# # print(soup.h2.text)

# f12 개발자 모드에서 selete elements후 상품 마우스 클릭 >
# result = soup.find_all("span", class_="sprinkles_fontSize_200_base__1byufe8uu sprinkles_fontWeight_regular__1byufe81x sprinkles_lineHeight_body.medium_base__1byufe8w6 sprinkles_color_neutral__1byufe81 f1uy1ch sprinkles_overflow_hidden__1byufe819")
# for item in result:
#     print(item.string)


# # bugs 사이트에서 음악 순위 크롤링
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# fr = urlopen("https://music.bugs.co.kr/chart?wl_ref=M_left_02_01")
# soup = BeautifulSoup(fr.read(), 'html.parser')

# # td 태그에 check라는 class가 있는 td 태그를 모두 가져온다
# musics = soup.find_all("td", "check")

# # musics의 각 태그들에 대해서
# for i, music in enumerate(musics):
#     # input 태그안에 title 속성값을 parsing한다.
#     print("{}위: {}".format(i + 1, music.input["title"]))

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('weather.csv', encoding='utf-8')

# # -----------------------------------
# # NaN값이 포함된 행을 지움
# weather.dropna(axis= 0, how="any", inplace=True)
# # NaN값이 포함된 행 출력
# print(weather[weather['평균풍속'].isna() == True])

# # -----------------------------------
# # NaN값의 기본값을 0으로 지정 
# weather.fillna(0, inplace=True)
# # 0인 값을 포함한 행 출력
# print(weather[weather['평균풍속'] == 0.0])

# # -------------------------------
# weather["최대풍속"].fillna(weather['최대풍속'].mean(), inplace=True)
# weather["평균풍속"].fillna(weather['평균풍속'].mean(), inplace=True)

# print(weather[weather["일시"] == "2012-02-11"])

data = {'key1': ['a', 'b', 'b', 'c', 'c'],
        'key2': ['v', 'w', 'w', 'x', 'y'],
        'col' : [1, 2, 3, 4, 5]}

df = pd.DataFrame(data, columns=['key1','key2','col'])

print(df.duplicated(['key1'],keep="first"))
print("----------------------")
print(df.duplicated(["key1","key2"]))