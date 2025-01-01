# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:52:16 2024

@author: Glesep
"""

# 시리즈에 함수 적용하기
import seaborn as sns
import numpy as np

df = sns.load_dataset('penguins')
bill_length_mm = df['bill_length_mm']

bill_length_mm.head()

# apply(): 시리즈의 모든 원소들에 함수를 적용
result = bill_length_mm.apply(np.sqrt)
result.head()

def mm_to_cm(num):
    return num / 10

result_2 = bill_length_mm.apply(mm_to_cm)
result_2.head()