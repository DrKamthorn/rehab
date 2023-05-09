import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import os

st.set_page_config(layout="wide")
st.title("เวชศาสตร์ฟื้นฟู กิจกรรมบำบัด")
st.title("ศูนย์การแพทย์กาญจนาภิเษก")

st.write("## ข้อมูล Frozen Shoulder ตั้งแต่ปี 2021")

@st.cache_data(ttl=3600)
def load_data():
	df_froz =pd.read_csv("frozen2.csv", error_bad_lines=False)

	return df_froz

df_froz=load_data()
num_shown=st.slider("จำนวนข้อมูลที่แสดง...",0,500,5)
st.table(df_froz[:num_shown])