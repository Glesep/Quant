# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:34:55 2024

@author: Glesep
"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')
df.head()

df_pivot_4 = df.pivot_table(index=['species', 'sex'],
                            columns='island',
                            values='bill_length_mm',
                            aggfunc='mean')

# stack(): 열 인덱스를 행 인덱스로 변환 - 시리즈 형태로 반환
df_pivot_4.stack()

# 위를 데이터프레임으로
df_pivot_4.stack().to_frame()

# unstack(): 행 인덱스를 열 인덱스로 변환
df_pivot_4.unstack()
