import pandas as pd
import numpy as np

# # p11 시리즈 클래스
# s1 = pd.Series([9904312, 3448737, 2890451, 2466052]
#              , index=['서울', '부산', '인천', '대구'])

# s1.name = '인구'
# s1.index.name = '도시'

# print(s1, '\n')
# print('대구 인구 = ', s1.대구)

# s2 = pd.Series(range(10, 14))

# print(s2)

# # p12 시리즈 연산
# s1 = pd.Series(range(3))
# s2 = pd.Series(range(3, 6))
# print(s1)

# print(s1 + s2)
# print(s1 / s2)

# # p13 시리즈 인덱싱

# s = pd.Series([9904312, 3448737, 2890451, 2466052],
#                 index=['서울', '부산', '인천', '대구'])
# print(s[3], s['대구'])
# print(s[[0, 3]], '\n', s[['서울', '대구']])
# print(s[(250e4 < s) & (s <= 500e4)])

# # p14 시리즈 슬라이싱
# print(s[1:3])
# print(s["부산":"대구"])

# # p15 데이터프레임 생성
# # 딕셔너리
# data = {
#     '2015': [9904312, 3448737, 2890451, 2466052],
#     '2010': [9631482, 3393191, 2632035, 2448736],
#     '2005': [9762546, 3512547, 2632035, 2485390],
#     '2000': [9853972, 3655437, 2466338, 2473990],
#     "지역": ['수도권', '경상권', '수도권', '경상권'],
#     "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
# }
# row = ['서울', '부산', '인천', '대구']
# col = ['지역', '2015', '2010', '2005', '2000', '2010-2015 증가율']

# df = pd.DataFrame(data, index=row, columns=col)

# print(df)
# # 2차원 배열
# data1 = [
#     ['홍', 25, '대구'],
#     ['김', 30, '부산'],
#     ['이', 22, '서울']
# ]
# df2 = pd.DataFrame(data1, columns=['이름', '나이', '지역'])
# print(df2)

# # excel 파일 읽기
# df3 = pd.read_excel('data.xlsx', sheet_name='data1', header=1,skipfooter=2)  # header=1 -> 2번째 줄을 헤더로 사용
# print(df3)

# # p16 데이터프레임 속성
# print(df.T)

# # p22 데이터프레임 슬라이싱
# df = pd.DataFrame(data, index=row, columns=col)
# print(df[1:3])
# print("--------------------------------")
# print(df['서울':'부산'])
# print("--------------------------------")
# print(df["2015"]["서울"], df["2015"][0])

# # p23 데이터프레임 loc 인덱서
# df = pd.DataFrame(np.arange(10, 22).reshape(3, 4),
#                   index=['r1', 'r2', 'r3'],
#                   columns=['A', 'B', 'C', 'D'])

# print(df); print("--------------------------------")
# print(df.loc['r2']); print("--------------------------------")
# print(df.loc['r2':'r3']); print("--------------------------------")

# # p24
# print(df.loc[:, :]); print("--------------------------------")
# print(df.loc["r2":"r3","B"]); print("--------------------------------")
# print(df.loc["r2":"r3","B" :"C"]); print("--------------------------------")
# print(df.loc["r2","B" :"C"]); print("--------------------------------")
# print(df.loc["r2","B"]); print("--------------------------------")

# # 실습
# df4 = pd.read_excel('data.xlsx', sheet_name='data2')
# print(df4.loc[df4.결제금액 > 20000,['이름','주소']])

# # p27 데이터프레임 열(시리즈) 갱신, 추가, 삭제

# df = pd.DataFrame(data, index=row, columns=col)
# df["2010-2015 증가율"] = df['2010-2015 증가율']  * 100
# df['2005-2015 증가율'] = ((df['2010'] - df['2005']) / df['2005'] * 100).round(2)
# print(df)

# df = pd.read_excel('data.xlsx', sheet_name='data2')
# df['사은품'] = df["결제금액"] >= 20000
# print(df)

# df['사은품'] = df['사은품'].map({True: '지급', False: '미지급'})
# print(df)

# df.to_excel('data.xlsx', index=False)

# p30~35 까지 10월31일에 함
# df = pd.read_csv('weather.csv', encoding='utf-8', index_col='일시')
# print(df.head())
# print("--------------------------------")
# print(df.tail())
# print("--------------------------------")
# print(df.describe())

# print("--------------------------------")
# print(df.count())
# print("--------------------------------")
# print(df.mean())
# print("--------------------------------")
# print(df['평균기온'].mean())
# print("--------------------------------")
# print(df.loc[df['평균풍속'] >= 4, '평균기온'].mean())

# --------------------------------
# 파이썬 특강 신청명단 (이름 및 학번 병합)
# python_df = pd.read_excel('특강신청명단.xlsx', sheet_name='파이썬특강') 
# students_df = pd.read_excel('특강신청명단.xlsx', sheet_name='학생목록') 
# merged_df = python_df.merge(students_df, how='left', on='학번') 
# print(merged_df) 
# merged_df.to_excel('파이썬.xlsx')

# ---------------------------------
# 파이썬 특강 신청명단
# python_df = pd.read_excel('특강신청명단.xlsx', sheet_name='파이썬특강') 
# students_df = pd.read_excel('특강신청명단.xlsx', sheet_name='학생목록') 
# merged_df = python_df.merge(students_df, how='left', on='학번') 
# merged_df.drop(columns=['이름_y'],inplace=True) 
# merged_df.rename(columns={'이름_x':'이름'}, inplace=True) 
# print(merged_df) 
# merged_df.to_excel('파이썬.xlsx')

# -------------------------------
# 자바 특강 신청여부
# java_df = pd.read_excel('특강신청명단.xlsx', sheet_name='자바특강') 
# students_df = pd.read_excel('특강신청명단.xlsx', sheet_name='학생목록') 
# merged_df = students_df.merge(java_df, how='left', indicator=True) 
# merged_df['자바특강'] = '' 
# merged_df.loc[merged_df['_merge'] == 'both', '자바특강'] = '신청' 
# merged_df = merged_df.drop(columns=['_merge']) 
# print(merged_df) 
# merged_df.to_excel('특강신청명단.xlsx', index=False)
# 또는 
# 자바 특강 신청여부
# merged_df2 = students_df.merge(java_df, how='left', indicator=True) 
# merged_df2['자바특강'] = np.where( 
# merged_df2['_merge'] == 'both', 
# '신청', 
# '' 
# ) 
# merged_df2 = merged_df2.drop(columns=['_merge']) 
# print(merged_df2)

# -------------------------------
# 파이썬 특강 신청여부
# python_df = pd.read_excel('특강신청명단.xlsx', sheet_name='파이썬특강')
# students_df = pd.read_excel('특강신청명단.xlsx', sheet_name='학생목록')
# merged_df3 = students_df.merge(python_df, how='left', indicator=True)
# merged_df3['파이썬특강'] = np.where(
#     merged_df3['_merge'] == 'both',
#     '신청',
#     ''
# )
# merged_df3 = merged_df3.drop(columns=['_merge'])
# print(merged_df3)
# merged_df3.to_excel('특강신청명단.xlsx', index=False)



# ------------------------------
# java_df = pd.read_excel('특강신청명단.xlsx', sheet_name='자바특강') 
# python_df = pd.read_excel('특강신청명단.xlsx', sheet_name='파이썬특강') 
# students_df = pd.read_excel('특강신청명단.xlsx', sheet_name='학생목록') 
# merged_df = students_df.merge(java_df, how='left', indicator=True) 
# merged_df['자바특강'] = '' 
# merged_df.loc[merged_df['_merge'] == 'both', '자바특강'] = '신청' 
# merged_df = merged_df.drop(columns=['_merge']) 
# merged_df = merged_df.merge(python_df, how='left', indicator=True) 
# merged_df['파이썬특강'] = '' 
# merged_df.loc[merged_df['_merge'] == 'both', '파이썬특강'] = '신청' 
# merged_df = merged_df.drop(columns=['_merge']) 
# print(merged_df) 
# merged_df.to_excel('모든과목.xlsx', index=False) 

# input_df = pd.read_excel('입력파일.xlsx', dtype=str) 
# input_df = input_df.drop(columns=['id', 'email', 'address', 'major', 'status']) 
# input_df = input_df.rename(columns={'studentNumber':'학번', 'studentName':'이름', 'contact':'연락처'}); 
# input_df.to_excel('출력파일.xlsx', index=False)


# ------------------------------
# orders_df = pd.read_excel('data3.xlsx') 
# orders_df['판매금액'] = orders_df['가격'] * orders_df['판매수량'] 
# # 카테고리별 총 판매액 
# category_sales = orders_df.groupby('카테고리')['판매금액'].sum().reset_index() 
# print(category_sales) 
# #카테고리별 총 판매 수량 
# category_stats = orders_df.groupby('카테고리').agg(총판매수량=('판매수량', 'sum')).reset_index() 
# print(category_stats)


# orders_df2 = pd.read_excel('data3.xlsx') 
# orders_df2['단가'] = orders_df2['가격'] / orders_df2['판매수량'] 
# orders_df2['부가세'] = orders_df2['가격'] * 0.1
# print(orders_df2.head())