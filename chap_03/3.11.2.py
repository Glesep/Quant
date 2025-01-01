# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:02:54 2024

@author: Glesep
"""

# 데이터프레임에 함수 적용하기
import pandas as pd
import seaborn as sns
import numpy as np

df = sns.load_dataset('penguins')
bill_length_mm = df['bill_length_mm']

df_num = df[['bill_length_mm', 'bill_depth_mm',
             'flipper_length_mm', 'body_mass_g']]

df_num.head()

# axis=0 방향으로 확인해서 함수를 적용
df_num.apply(max)

# axis=1 방향으로 확인해서 함수를 적용
df_num.apply(max, axis=1)

def num_null(data):
    null_vec = pd.isnull(data)
    null_count = np.sum(null_vec)
    
    return null_count

df_num.apply(num_null)
