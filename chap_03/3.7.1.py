# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 12:02:56 2024

@author: Glesep
"""

import pandas as pd
import seaborn as sns

# 불리언 인덱싱

# 데이터셋 불러오기
df = sns.load_dataset('mpg')
df.tail(10)

# unique() 메서드는 고유한 값을 반환
df['cylinders'].unique()

# 불리언 시리즈 제작
filter_bool = (df['cylinders'] == 4)
filter_bool.tail(10)

# 행 인덱스에 불리언 시리즈를 입력하여 해당 조건을 만족하는 행만 선택
df.loc[filter_bool, ]

# 조건을 여러 개 입력 가능
filter_bool_2 = (df['cylinders'] == 4) & (df['horsepower'] >= 100)
# 열 이름을 리스트 형태로 입력하면 해당 열만 선택됨
df.loc[filter_bool_2, ['cylinders', 'horsepower', 'name']]
