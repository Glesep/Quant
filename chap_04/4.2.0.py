# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:34:27 2024

@author: Glesep
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('penguins')

# 산점도 그리기
# plt.scatter(x축, y축)
plt.scatter(df['flipper_length_mm'], df['body_mass_g'])
plt.show()


# 막대 그래프 그리기
# species별로 그룹을 묶은 후 'body_mass_g' 열의 평균을 구하기
df_group = df.groupby('species')['body_mass_g'].mean().reset_index()
# plt.bar(x=x축, height=높이 정보)
plt.bar(x=df_group['species'], height=df_group['body_mass_g'])
plt.show()


# 히스토그램 그리기
# matplotlib은 한글 폰트를 지원 X, 한글이 깨지지 않도록 'Malgun Gothic' 폰트 지정
plt.rc('font', family='NanumSquare')
# plt.hist(나타내고자 하는 데이터, bins=히스토그램을 몇 개의 구간으로 나눌지 입력)
plt.hist(df['body_mass_g'], bins=30)
# x, y축 레이블 설정
plt.xlabel('Body Mass')
plt.ylabel('Count')
# 제목 설정
plt.title('팽귄의 몸무게 분포')
plt.show()

import matplotlib.font_manager as fm

SHARE_PATH = "/usr/share/fonts"
font_name = fm.FontProperties(
    fname=f"{SHARE_PATH}/truetype/nanum/NanumSquare.ttf"
).get_name()
plt.rc("font", family=font_name)

import sys
sys.path.append(f"{SHARE_PATH}")

