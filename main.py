import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import st_folium

plt.rcParams['font.family'] ='D2Coding'

with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Projects", "Map", "Entering" ,"Contact"],
    icons = ["house","rocket","map", "door" ,"envelope"],
    menu_icon = "cast",
    default_index = 0,

  )
st.title("지식산업센터 현황분석 대시보드")


# 데이터 가져오기 df
df = pd.read_csv('Knowledge_Center.csv', encoding="CP949")


if selected == "Home":
    st.header("Welcome InnovationPARK !!")

elif selected == "Projects":
    st.header(":church: 지역별 지식산업센터 수")

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
        folium.Marker([row['위도'], row['경도']], tooltip=row['지식산업센터명칭']).add_to(m)

    # Streamlit에서 지도 표시
    st_folium(m, width=700, height=500)





elif selected == "Entering":
    st.header("지역별 입주율(선택지역)")

    # 지역별 지식산업센터 수 집계
    df['입주율'] = pd.to_numeric(df['입주율'], errors='coerce')
    df.fillna({'입주율': 0}, inplace=True)
    
    
    region_counts = df['입주율'].value_counts()

    # 사용자가 '시군명'을 선택할 수 있는 드롭다운 메뉴 생성
    unique_regions = df['시군명'].unique()
    selected_region = st.selectbox("지역을 선택하세요", unique_regions)

    # 선택된 지역에 대한 데이터 필터링
    filtered_df = df[df['시군명'] == selected_region]

    
    average_occupancy_rate = filtered_df['입주율'].mean()

    # 결과 시각화
    st.write(f"{selected_region} 지역의 평균 입주율: {average_occupancy_rate:.2f}%")

    # # 결과 시각화
    plt.figure(figsize=(4, 3))
    plt.bar(selected_region, average_occupancy_rate)
    plt.title(f"{selected_region} 지역의 평균 입주율")
    plt.xlabel('지역')
    plt.ylabel('평균 입주율')
    st.pyplot(plt)


    st.header("지역별 입주율(전체지역)")
    ## 입주율이 0.1 이상인 지역들만 필터링
    filtered_df = df[df.groupby('시군명')['입주율'].transform('mean') > 0.1]

    # 필터링된 데이터를 기반으로 평균 입주율 계산
    average_entering_rate = filtered_df.groupby('시군명')['입주율'].mean()

    # 결과 시각화
    plt.figure(figsize=(10, 6))
    plt.bar(average_entering_rate.index, average_entering_rate.values)
    # plt.axhline(y=average_entering_rate, color='r', linestyle='--')
    plt.title('지역별 평균 입주율')
    plt.xlabel('지역')
    plt.ylabel('입주율')
    st.pyplot(plt)
    



# elif selected == "Contact":
#     st.header("연락처")
#     # 연락처 정보 또는 양식을 여기에 추가
#     st.write("01074252558")

# st.header("지역별 입주율(전체지역)")
# ## 입주율이 0.1 이상인 지역들만 필터링
# filtered_df = df[df['입주율'] > 0.1]

# # 필터링된 데이터를 기반으로 평균 입주율 계산
# average_entering_rate = filtered_df.groupby('시군명')['입주율'].mean()

# # 결과 시각화
# plt.figure(figsize=(10, 6))
# plt.bar(average_entering_rate.index, average_entering_rate.values)
# # plt.axhline(y=average_entering_rate, color='r', linestyle='--')
# plt.title('지역별 평균 입주율')
# plt.xlabel('지역')
# plt.ylabel('입주율')
# st.pyplot(plt)