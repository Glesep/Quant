# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:53:36 2024

@author: Glesep
"""

import seaborn as sns

df = sns.load_dataset('mpg')
# 데이터 확인 시, 일반적으로 인덱스에는 위치 인덱스가 입력됨
df.head()

# 인덱스를 자동차 이름인 name열으로 설정
df.set_index('name', inplace=True)
df.head()

# 인덱스 정렬 - 기본:오름차순
df.sort_index(inplace=True)
df.head()

# 인덱스 정렬 - 내림차순
df.sort_index(inplace=True, ascending=False)
df.head()

# 인덱스를 원래대로 설정 - 기존에 존재했던 인덱스는 다시 하나의 열로 돌아감
df.reset_index(inplace=True)
df.head()