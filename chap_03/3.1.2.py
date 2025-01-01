# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:09:37 2024

@author: Glesep
"""

import pandas as pd

capital = pd.Series({'Korea' : 'Seoul',
                     'Japan' : 'Tokyo',
                     'China' : 'Beijing',
                     'India' : 'New Delhi',
                     'Taiwan' : 'Taipei',
                     'Singapore' : 'Singapore'
                    })
print(capital)

# 한국에 해당하는 데이터 선택 - 시리즈에서는 인덱스의 이름을 입력하면 해당되는 값이 선택된다.
capital['Korea']

# 값을 찾고 싶은 인덱스를 리스트 형태로 입력하면 이에 해당하는 모든 원소 선택
capital[['Korea', 'Taiwan']]

# 시리즈의 위치를 통해서도 원하는 값을 선택 가능
capital[0]

# 위치 인덱스를 리스트형태로 입력하면 해당되는 모든 원소 선택됨
capital[[0, 3]]

# 리스트와 동일하게 슬라이싱 기능 사용 가능 - 범위: [, )
capital[0:3]


# 시리즈끼리는 사칙연산이 가능하다.
series_1 = pd.Series([1, 2, 3])
series_2 = pd.Series([4, 5, 6])

series_1 + series_2

series_1 * 2
