# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:20:51 2024

@author: Glesep
"""
# 데이터 재구조화

import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')
df.head()

# melt(): id_vars를 기준으로 id_vars를 제외한 원본 데이터프레임 열 이름들을 variable 열에 넣고, 각 열에 있는 데이터들은 value열에 넣은 형태로 만듦
df.melt(id_vars=['species', 'island']).tail(10)
