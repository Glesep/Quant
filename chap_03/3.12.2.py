# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:24:43 2024

@author: Glesep
"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')
df.head()

df_group = df.groupby(['species'])

# 그룹별 연산하기 - 그룹 객체에서 숫자열 선택 후 메서드 적용
df_group[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].mean()

# 그룹의 기준을 하나가 아닌 여러 열로 설정 가능
df.groupby(['species', 'sex'])[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].mean()


# 집계 연산을 처리한느 함수를 사용자가 직접 만든 후 그룹 객체에 적용 - agg() 사용
def min_max(x):
    return x.max() - x.min()

df.groupby(['species'])['bill_length_mm'].agg(min_max)

# agg()를 사용하면 한 번에 여러 개의 집계 연산 사용 가능
df.groupby(['species'])[[
    'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].agg(['max', 'min'])

# 각 열마다 다른 종류의 함수를 적용 가능
df.groupby(['species']).agg({'bill_length_mm':['max', 'min'],
                             'island':['count']})


# transform(): 그룹별로 함수를 적용하는 것은 동일, 그 결과를 본래의 행 인덱스나 열 인덱스를 기준으로 반환
df.groupby(['species'])['bill_length_mm'].transform('mean')

def z_score(x):
    z = (x-x.mean()) / x.std()
    return(z)

df.groupby(['species'])['bill_length_mm'].transform(z_score)


# apply() 메서드를 그룹 객체에 적용 가능
df.groupby(['species'])['bill_length_mm'].apply(min)
# 사용자 함수는 tranform()을 사용한 것과 결과가 동일
df.groupby(['species'])['bill_length_mm'].apply(z_score)


# filter(): 조건에 해당하는 그룹만 반환
df.groupby(['species']).filter(lambda x: x['bill_length_mm'].mean() >= 40)