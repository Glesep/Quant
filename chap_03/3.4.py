# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 00:16:29 2024

@author: Glesep
"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

# 데이터의 맨 위 살펴보기
#   -> head 내의 숫자만큼 위에서부터 행을 보여줌, 값 입력하지 않을 시 5개 출력
df.head()

# 데이터의 맨 아래 살펴보기
#   -> head 내의 숫자만큼 아래에서부터 행을 보여줌, 값 입력하지 않을 시 5개 출력
df.tail()

# 데이터프레임의 크기 확인 - (행 개수, 열 개수)
df.shape

# 데이터프레임 기본 정보 확인
df.info()

# 긱 열의 고윳값 개수 구하기 - sex의 고윳값 종류, 개수 알아보기
df['sex'].value_counts()

# 다중 열을 기준으로 value_counts() 사용
df[['sex', 'survived']].value_counts()

# 위의 메서드에서 데이터를 정렬, 개수를 비중으로 바꿔서 출력
df[['sex', 'survived']].value_counts(normalize=True).sort_index()

# 원하는 열을 선택 후 산술평균 계산
df['survived'].mean()

# 여러개의 열을 리스트 형태로 입력하여 동시에 평균 구하기
df[['survived', 'age']].mean()

# 극단적인 값이 존재할 경우 산술평균은 왜곡가능
# 최솟값 확인
df['fare'].min()
# 최댇값 확인
df['fare'].max()

# 최솟값 : 0.0, 최댓값 512.3292 - 차이가 심하게 남 -> 산술평균 왜곡가능
# 따라서 중위값을 같이 봐야 함
df['fare'].mean()
df['fare'].median()
