# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:42:12 2024

@author: Glesep
"""

# isin() method

import pandas as pd
import seaborn as sns

df = sns.load_dataset('mpg')

# 특정 값을 가진 데이터를 선택하려고 함

# 불리언 인덱싱
filter_bool_3 = (df['name'] == 'ford maverick')|(df['name'] == 'ford mustang ii')|(df['name'] == 'chevrolet impala')
                
df.loc[filter_bool_3, ]

# isin() 메소드
filter_isin = df['name'].isin(
    ['ford maverick', 'ford mustang ii', 'chevrolet impala'])
df.loc[filter_isin, ]

# horsepower열을 기준으로 오름차순 정렬(기본), 내림차순: ascending=False
df.loc[filter_isin, ].sort_values('horsepower')
