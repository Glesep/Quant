# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 00:05:21 2024

@author: Glesep
"""

import pandas as pd

# csv 파일을 데이터프레임 형식으로 불러오기
data_csv = pd.read_csv(
    'https://raw.githubusercontent.com/hyunyulhenry/quant_py/main/kospi.csv')

# 데이터프레임을 csv 파일로 저장하기
data_csv.to_csv('data.csv')

# ============================================================================

# 엑셀 파일을 데이터프레임 형식으로 불러오기
#   - 시트명을 입력하지 않으면 가장 첫 번째 시트의 데이터를 불러옴
#   - sheet_name을 통해 불러오고자 하는 시트 선택
data_excel = pd.read_excel(
    'https://github.com/hyunyulhenry/quant_py/raw/main/kospi.xlsx', sheet_name='kospi')

# 데이터프레임을 엑셀 파일로 저장하기
data_excel.to_excel('data.xlsx')
