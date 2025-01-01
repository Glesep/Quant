# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:34:55 2024

@author: Glesep
"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset("taxis")

# pickup 열과 dropoff열을 보면 시계열 형태로 보임
df.head()

# 판다스에서 object - 문자열
df.info()

# 판다스에서 to_datetime() 메서드를 통해 문자열을 datetime 객체로 변환 가능
df['pickup'] = pd.to_datetime(df['pickup'])
df['dropoff'] = pd.to_datetime(df['dropoff'])

df.info()


# pickup 열에서 연도에 해당하는 정보만 추출
df['pickup'][0].year

# pickup 열에 존재하는 모든 데이터의 연도를 추출 - dt 접근자를 이용
df['year'] = df['pickup'].dt.year
df['month'] = df['pickup'].dt.month
df['day'] = df['pickup'].dt.day
df['date'] = df['pickup'].dt.date

df[['pickup', 'year', 'month', 'day', 'date']].head()


# pickup 열을 기준으로 정렬
df.sort_values('pickup', inplace=True)
df.reset_index(drop=True, inplace=True)

df.head()

# 운행 시간 계산 - pickup 열과 dropoff 열의 차이 구하기
# datetime 객체끼리는 시간에 대해 연산 가능
df['dropoff'] - df['pickup']

# pickup 열을 행 인덱스로 변경
df.set_index('pickup', inplace=True)
df.head()

# 인덱스의 타입을 확인 - 인덱스가 DatetimeIndex 형태
df.index

# 인덱스가 DatetimeIndex 형태 -> 원하는 날짜 또는 시간의 데이터를 바로 추출 가능
# 2019년 2월 데이터 추출
df.loc['2019-02']

# 2019년 3월 1일 ~ 2019년 3월 2일 데이터 추출
df.loc['2019-03-01':'2019-03-02']

# =============================================================================

# 시계열 데이터 만들기

# date_range(start: 시작일, end: 종료일, freq: 간격)
pd.date_range(start='2021-01-01',
              end='2021-12-31',
              freq='M')

# 3D는 3일을 의미, 3일 주기의 시계열 데이터 제작
pd.date_range(start='2021-01-01',
              end='2021-12-31',
              freq='3D')

# W는 주, MON은 월요일을 뜻함 - 매주 월요일에 해당하는 날짜가 시계열 데이터로 제작됨
pd.date_range(start='2021-01-01',
              end='2021-01-31',
              freq='W-MON')

# WOM은 Week Of Month, 2THU는 둘째 주 목요일을 뜻함 - 매월 둘째 주 목요일
pd.date_range(start='2021-01-01',
              end='2021-12-31',
              freq='WOM-2THU')