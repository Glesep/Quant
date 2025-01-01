# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:17:11 2024

@author: Glesep
"""

import pandas as pd

df1 = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"]
    },
    index=[0,1,2,3],
)

df2 = pd.DataFrame({
    "A": ["A4", "A5", "A6", "A7"],
    "B": ["B4", "B5", "B6", "B7"],
    "C": ["C4", "C5", "C6", "C7"],
    "D": ["D4", "D5", "D6", "D7"]
    },
    index=[4, 5, 6, 7],
)

df3 = pd.DataFrame({
    "A": ["A8", "A9", "A10", "A11"],
    "B": ["B8", "B9", "B10", "B11"],
    "C": ["C8", "C9", "C10", "C11"],
    "D": ["D8", "D9", "D10", "D11"]
    },
    index=[8, 9, 10, 11],
)

# 행 방향(행을 쌓는 방식)으로 데이터프레임이 합쳐진다.
result = pd.concat([df1, df2, df3])
result

df4 = pd.DataFrame({
    "B": ["B2", "B3", "B6", "B7"],
    "D": ["D2", "D3", "D6", "D7"],
    "F": ["F2", "F3", "F6", "F7"]
    },
    index=[2,3,6,7]
)

# 열 이름이 합집합을 기준으로 생성됨, 해당하는 열에 데이터가 없으면 NaN으로 채워짐
# 행 인덱스는 유지됨
result = pd.concat([df1, df4])

# 행 인덱스를 초기화하고 싶으면 ignore_index=True입력
result = pd.concat([df1, df4], ignore_index=True)


# 행이 아닌 열 기준으로 데이터 합치기(합집합) - 열을 쌓는다고 생각(오른쪽으로)
result = pd.concat([df1, df4], axis=1)

result = pd.concat([df1, df4], axis=1, join="inner")
result


# 데이터프레임에 시리즈도 합칠 수 있음
s1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")
result = pd.concat([df1, s1], axis=1)

result























