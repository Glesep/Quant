# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:38:49 2024

@author: Glesep
"""

import pandas as pd

dict_data = {'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8],
             'col3': [9, 10, 11, 12], 'col4': [13, 14, 15, 16]}

# index == 행의 인덱스
df = pd.DataFrame(dict_data, index=['index1', 'index2', 'index3', 'index4'])

# DataFrame에서 열 선택하기
#   1. df['열 이름']
#   2. df.열 이름 (열 이름이 문자열인 경우에만 사용 가능)
df['col1']
df.col1

# 열을 한 개만 선택할 경우 시리즈 객체 반환
type(df['col1'])

# 만일 데이터프레임 객체로 반환을 원할 경우
df[['col1']]
type(df[['col1']])

# 데이터프레임에서 2개 이상의 열 추출
#   - df[['열 이름 1', '열 이름 2' ...]]
df[['col1', 'col2']]

# ==============================================================

# DataFrame에서 행 선택하기
#   1. df.loc['행 인덱스']
#   2. df.iloc[행 위치 인덱스]
df.loc['index1']
df.iloc[0]

# 행을 한 개만 선택할 경우 시리즈 객체 반환
type(df.loc['index1'])

# 만일 데이터프레임 객체로 반환을 원할 경우
df.loc[['index1']]
df.iloc[[0]]
type(df.loc[['index1']])

# 인덱서 사용 시 슬라이싱 기능 사용 가능
# df.loc의 경우 범위 - [ , ]
#   -> 이름으로 정확히 명시했으니 둘 다 들어간다고 생각
# df.iloc의 경우 범위 - [ , )
#   -> 국룰 범위
df.loc['index1' : 'index3']
df.iloc[0:2]

# ==============================================================

# DataFrame에서 행과 열을 동시에 입력하여 원하는 원소 선택하기
#   1. df.loc['행 인덱스', '열 인덱스']
#   2. df.iloc[행 위치, 열 위치]
df.loc['index1', 'col1']
df.iloc[0, 0]

# 하나가 아닌 여려 원소 선택 가능
df.loc[['index1', 'index3'], ['col1', 'col4']]
df.iloc[[0, 2], [0, 3]]

# 슬라이싱을 이용해서도 원소 선택 가능
df.loc['index1':'index2', 'col1':'col3']
df.iloc[0:2, 0:3]