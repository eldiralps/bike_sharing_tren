import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np


sns.set(style='dark')

# load data
rental_bike_hour_df = pd.read_csv("rental_bike_hour_df.csv")
rental_bike_day_df = pd.read_csv("rental_bike_day_df.csv")
df_2011 = pd.read_csv("df_2011.csv")
df_2012 = pd.read_csv("df_2012.csv")

st.title('Dashboard Trend of Bike Sharing during 2011-2012 :sparkles:')
st.write("Nama          : Eldira Lahanny Permata Sherman")
st.write("Email         : eldiralps@gmail.com")
st.write("ID Dicoding   : eldiralps")
page1, page2, page3 = st.tabs(['Peak Hour of Bike Sharing', "Trend of Bike Sharing based on The Season", "Time Series Forecasting of Bike Sharing"])

# TAB 1
with page1:
    st.header('Peak Hour of Bike Sharing')

    st.subheader("Bike Sharing Trend for All User")
    st.image("count.jpg", use_column_width=True)

    st.subheader("Bike Sharing Trend for Registered User")
    st.image("registered.jpg", use_column_width=True)

    st.subheader("Bike Sharing Trend for Casual User")
    st.image("casual.jpg", use_column_width=True)
    


# TAB 2
with page2:
    st.header("Trend of Bike Sharing based on The Season")

    st.subheader("Bike Sharing Trend in 2011")
    st.image("2011.jpg", use_column_width=True)
    st.write("Keterangan: warna background putih menandakan musim Spring")

    st.subheader("Bike Sharing Trend in 2012")
    st.image("2012.jpg", use_column_width=True)
    st.write("Keterangan: warna background putih menandakan musim Spring")

with page3:
    st.header("Time Series Forecasting of Bike Sharing using EMA Method")

    st.subheader("Time Series Forecasting for alpha = 0.75")
    st.image("alpha_075.jpg", use_column_width=True)

    st.subheader("Time Series Forecasting for alpha = 0.2")
    st.image("alpha_02.jpg", use_column_width=True)

st.caption('Copyright (c) Eldira Lahanny Permata Sherman 2024')
