# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:15:08 2024

@author: Glesep
"""

# join() - merge와 사용법 비슷
# merge(): 키를 기준으로 결합 / join(): 행 인덱스를 기준으로 결합

import pandas as pd

left = pd.DataFrame({
    
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"]},
    index=["K0", "K1", "K2", "K3"]
)

right = pd.DataFrame({
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"]},
    index=["K0", "K1", "K3", "K4"]
)

# join() 은 디폴트로 left join 방법 사용
result = left.join(right)
