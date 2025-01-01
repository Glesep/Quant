# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:59:37 2024

@author: Glesep
"""

import pandas as pd

dict_data = {'a' : 1, 'b' : 2, 'c' : 3}
series = pd.Series(dict_data)

print(series)


series.index
series.values


list_data = ['a', 'b', 'c']
series_2 = pd.Series(list_data)     # 인덱스는 정수형 위치 인덱스가 자동으로 지정

print(series_2)

series_3 = pd.Series(list_data, index=['index1', 'index2', 'index3'])
print(series_3)