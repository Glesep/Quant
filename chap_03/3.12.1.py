# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:13:25 2024

@author: Glesep
"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')
df.head()

# 그룹 나누기 - 기준 열 내부에서 같은 값을 가진 요소들끼리 모아줌
df_group = df.groupby(['species'])
df_group.head()

for key, group in df_group:
    print(key)
    display(group.head(2))

