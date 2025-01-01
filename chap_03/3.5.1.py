# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:17:31 2024

@author: Glesep
"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

# df.info(): 정보 확인, not-null count를 볼 수 있다.
df.info()

# isnull(): 결측치면 True, 유효 데이터면 False
# notnull(): isnull()과 반대
df.head().isnull()

# df.dropna(): 데이터가 결측치가 있을 경우 해당 행(기본값)을 모두 삭제
df.dropna()

# dropna 메서드 내에 subset을 입력하면 해당 열 중 결측치가 있는 경우 행을 삭제(axis=0)한다.
df.dropna(subset=['age'], axis=0)

# 결측치가 있는 열을 삭제하고 싶으면 axis=1
df.dropna(axis=1)

# 결측치 개수의 기준치를 설정 가능: thresh
# thresh=300: 결측치가 300개 이상을 갖는 곳(axis)을 삭제
df.dropna(axis=1, thresh=300)


