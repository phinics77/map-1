import streamlit as st
from streamlit_folium import st_folium  # 변경됨
import folium
from folium.plugins import MarkerCluster
import pandas as pd

st.title("진주시 CCTV 현황")

# CSV 읽기
df = pd.read_csv("경상남도 진주시_CCTV위치정보_20250501.csv", encoding='euc-kr')

# 컬럼 정리
df.rename(columns=lambda x: x.strip(), inplace=True)
df[["lat", "lon"]] = df[["위도", "경도"]]

st.dataframe(df, height=200)

# 지도 생성
m = folium.Map(location=[35.1799817, 128.1076213], zoom_start=13)
marker_cluster = MarkerCluster().add_to(m)

for idx, row in df.iterrows():
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=row["설치장소"],
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(marker_cluster)

# 지도 출력
st_folium(m)
