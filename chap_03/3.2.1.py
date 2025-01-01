# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:21:29 2024

@author: Glesep
"""
import pandas as pd

# 딕셔너리의 키는 열의 이름, 딕셔너리의 값은 열의 값
dict_data = {'col1' : [1, 2, 3], 'col2' : [4, 5, 6], 'col3' : [7, 8, 9]}
df = pd.DataFrame(dict_data)


# 각 리스트가 행의 형태로 입력, 데이터프레임의 행과 열은 위치 인덱스가 됨
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 데이터프레임 정의 시, index(행의 이름)과 columns(열의 이름) 지정
df3 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                   index = ['index1', 'index2', 'index3'],
                   columns=['col1', 'col2', 'col3'])

# 기존 데이터프레임 행 인덱스와 열 이름도 변경 가능
df3.index = ['행 1', '행 2', '행 3']
df3.columns = ['열 1', '열 2', '열 3']

# 기존 데이터프레임 행 인덱스와 열 이름을 각각 변경 - inplace는 df3에 바로 적용한다는 뜻
df3.rename(index={'행 1': '첫 번째 행'}, inplace=True)
df3.rename(columns={'열 1': '첫 번째 열'}, inplace=True)

# 행 삭제 : DataFrame.drop(행 인덱스, axis=0, inplace=True)
# 열 삭제 : DataFrame.drop(열 이름, axis=1, inplace=True)
df3.drop('행 3', axis=0, inplace=True)
df3.drop('열 3', axis=1, inplace=True)