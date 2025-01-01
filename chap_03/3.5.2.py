# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:32:19 2024

@author: Glesep
"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

# 데이터프레임 복사
df_2 = df.copy()

df_2.head(6)


mean_age = df_2['age'].mean()
print(mean_age)

# fillna(): 결측치를 특정 값으로 대체, inplace=True: 원본 객체 변경
"""
FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
"""
df_2['age'].fillna(mean_age, inplace=True)

# 결측치가 채워졌는지 확인
df_2['age'].head(6)

# fillna()를 통해 숫자가 아닌 문자로 변경 가능
df_2['embark_town'].fillna('Southampton', inplace=True)

# 결측치를 결측치가 아닌 직전/직후 행의 값으로 변경: fillna(method='ffill' or 'bfill')
"""
FutureWarning: Series.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
  df_2['deck_ffill'] = df_2['deck'].fillna(method='ffill')
"""
df_2['deck_ffill'] = df_2['deck'].fillna(method='ffill')
df_2['deck_bfill'] = df_2['deck'].fillna(method='bfill')

df_2[['deck', 'deck_ffill', 'deck_bfill']].head(12)