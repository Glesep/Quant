# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:56:04 2024

@author: Glesep
"""

import pandas as pd

# merge() 함수

left = pd.DataFrame({
    "key": ["K0", "K1", "K2", "K3"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"]
})

right = pd.DataFrame({
    "key": ["K0", "K1", "K3", "K4"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"]
})

# inner join: 기준이 되는 열을 on=에 입력, 기준열의 교집합에 해당하는 데이터가 속한 행만 열 방향으로 합쳐짐
# merge 함수의 기본 값
result = pd.merge(left, right, on="key")


# left join: 왼쪽 데이터프레임은 유지, 오른쪽 데이터프레임이 키를 기준으로 합쳐짐
result = pd.merge(left, right, on="key", how="left")

# right join: 왼쪽 데이터프레임은 유지, 오른쪽 데이터프레임이 키를 기준으로 합쳐짐
result = pd.merge(left, right, on="key", how="right")

# outer join: 데이터프레임 중 어느 한쪽에만 속하더라도 상관없이 합집합 부분을 반환
result = pd.merge(left, right, on="key", how="outer")

# 기준이 되는 열의 이름이 서로 다른 경우는 left_on과 right_on을 통해 키를 직접 선언
left = pd.DataFrame({
    "key_left": ["K0", "K1", "K2", "K3"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"]
})

right = pd.DataFrame({
    "key_right": ["K0", "K1", "K3", "K4"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"]
})

result = pd.merge(left, right, left_on='key_left',
                      right_on='key_right', how='inner')

# merge(left, right) -> left.merge(right) 가능
result = left.merge(right, left_on='key_left',
                      right_on='key_right', how='inner')