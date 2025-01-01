# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:26:22 2024

@author: Glesep
"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')
df.head()

# pivot_table() - 총 4개 입력값이 필요함
# index: 행 인덱스, columns: 열 인덱스, values: 데이터 값, aggfunc: 데이터 집계 함수

# 팽귄 데이터의 species와 island별로 bill_length_mm의 평균 구하기
df_pivot_1 = df.pivot_table(index='species',
                            columns='island',
                            values='bill_length_mm',
                            aggfunc='mean')

# 복수의 조건 입력은 리스트로
df_pivot_2 = df.pivot_table(index=['species', 'sex'],
                            columns='island',
                            values=['bill_length_mm', 'flipper_length_mm'],
                            aggfunc=['mean', 'count'])