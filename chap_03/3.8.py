# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:49:53 2024

@author: Glesep
"""

# 새로운 열 만들기

import pandas as pd
import seaborn as sns

df = sns.load_dataset('mpg')

# 시리즈끼리 연산을 할 수 있음을 이용, 새로운 열 만들기
df['ratio'] = (df['mpg'] / df['weight']) * 100
df.head()

# 특정 열의 조건을 기반으로 새로운 열을 만들 수 있음
import numpy as np

num = pd.Series([-2, -1, 1 ,2])

# where(): 조건이 True인 지점의 인덱스를 반환
np.where(num >= 0)
# where(조건, 참, 거짓): 조건이 True이면 참에 해당하는 인자를 부여, False이면 거짓에 해당하는 인자를 부여
np.where(num >= 0, '양수', '음수')


# 위를 이용하여 horsepower가 100미만, 100이상, 200이상인지를 구분하는 열 제작
# np.where을 중첩
df['horse_power_div'] = np.where(
    df['horsepower'] < 100, '100 미만',
    np.where((df['horsepower'] >= 100) & (df['horsepower'] < 200), '100 이상',
             np.where(df['horsepower'] >= 200, '200 이상', '기타')))
df.head(8)