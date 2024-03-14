import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from streamlit_option_menu import option_menu

plt.rcParams['font.family'] ='Malgun Gothic'

with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Projects","Contact"],
    icons = ["house","book","envelope"],
    menu_icon = "cast",
    default_index = 0,

  )
st.title("지식산업센터 현황분석 대시보드")



# 데이터 가져오기 df
df = pd.read_csv('Knowledge_Center.csv', encoding="CP949")


#

