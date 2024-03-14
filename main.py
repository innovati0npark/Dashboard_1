import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import st_folium

plt.rcParams['font.family'] ='Malgun Gothic'

with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Projects", "Map", "Contact"],
    icons = ["house","rocket","map","envelope"],
    menu_icon = "cast",
    default_index = 0,

  )
st.title("지식산업센터 현황분석 대시보드")


# 데이터 가져오기 df
df = pd.read_csv('Knowledge_Center.csv', encoding="CP949")


if selected == "Home":
    st.header("Welcome InnovationPARK !!")

elif selected == "Projects":
    st.header(":church:지역별 지식산업센터 수")

    # 지역별 지식산업센터 수 집계
    region_counts = df['시군명'].value_counts()

    # 막대 그래프 그리기(지역별 수)
    plt.figure(figsize=(10, 6))
    region_counts.plot(kind='bar')
    plt.title('지역별 지식산업센터 수')
    plt.xlabel('지역')
    plt.ylabel('개수')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    st.header(":round_pushpin:지식산업센터 용도별 수")

    # 지역별 지식산업센터 수 집계
    region_counts = df['용도지역'].value_counts()

    # 막대 그래프 그리기(용도별 수)
    plt.figure(figsize=(10, 6))
    region_counts.plot(kind='pie')
    plt.title('지식산업센터 용도지역별 수')
    plt.xlabel('용도명칭')
    plt.ylabel('비율')
    plt.xticks(rotation=45)
    st.pyplot(plt)


elif selected == "Map":
    # Map으로 보여주기
    st.title('위도와 경도 데이터로 지식산업센터 위치 표시')

    # 기본 지도 생성 (한국 중심으로 설정)
    m = folium.Map(location=[36, 128], zoom_start=7)

    # 데이터프레임의 각 행에 대하여 위치를 지도에 표시
    for idx, row in df.iterrows():
        folium.Marker([row['위도'], row['경도']]).add_to(m)

    # Streamlit에서 지도 표시
    st_folium(m, width=700, height=500)

elif selected == "Contact":
    st.header("연락처")
    # 연락처 정보 또는 양식을 여기에 추가
    st.write("01074252558")


