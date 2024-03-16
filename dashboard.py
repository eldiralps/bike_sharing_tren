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
page1, page2 = st.tabs(['Peak Hour of Bike Sharing', "Trend of Bike Sharing based on The Season"])

# TAB 1
with page1:
    st.header('Peak Hour of Bike Sharing')

    st.subheader("Bike Sharing Trend for All User")
    fig1, ax1 = plt.subplots(figsize = (20,5))
    sns.pointplot(data = rental_bike_hour_df , x =np.array(rental_bike_hour_df['hours']) , y =np.array(rental_bike_hour_df['count']), hue = 'day_mapped', ax=ax1)
    ax1.set(title='Count of bike sharing demand during weekdays and weekends')
    st.pyplot(fig1)

    st.subheader("Bike Sharing Trend for Registered User")
    fig2 , ax2 = plt.subplots(figsize = (20,5))
    sns.pointplot(data = rental_bike_hour_df , x = np.array(rental_bike_hour_df['hours']), y = np.array(rental_bike_hour_df['registered']), hue = 'day_mapped', ax=ax2)
    ax2.set(title = 'Count of bike sharing demand during weekdays and weekends: registered users')
    st.pyplot(fig2)

    st.subheader("Bike Sharing Trend for Casual User")
    fig3 , ax3 = plt.subplots(figsize = (20,5))
    sns.pointplot(data = rental_bike_hour_df , x = np.array(rental_bike_hour_df['hours']), y = np.array(rental_bike_hour_df['casual']), hue = 'day_mapped', ax=ax3)
    ax3.set(title = 'Count of bike sharing demand during weekdays and weekends: casual users')
    st.pyplot(fig3)


# TAB 2
with page2:
    st.header("Trend of Bike Sharing based on The Season")

    st.subheader("Bike Sharing Trend in 2011")
    # Kelompokkan data berdasarkan musim
    summer_2011 = df_2011[df_2011['season_mapped'] == 'Summer']
    fall_2011 = df_2011[df_2011['season_mapped'] == 'Fall']
    winter_2011 = df_2011[df_2011['season_mapped'] == 'Winter']
    spring_2011 = df_2011[df_2011['season_mapped'] == 'Spring']

    # Plot jumlah pengguna setiap bulannya
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    ax4.plot(np.array(df_2011['month_mapped']), np.array(df_2011['count']), color='black', label='Total Users')

    # Tambahkan background untuk setiap musim
    ax4.fill_between(np.array(summer_2011['month_mapped']), np.array(summer_2011['count']), color='yellow', alpha=0.3, label='Summer')
    ax4.fill_between(np.array(fall_2011['month_mapped']), np.array(fall_2011['count']), color='orange', alpha=0.3, label='Fall')
    ax4.fill_between(np.array(winter_2011['month_mapped']), np.array(winter_2011['count']), color='blue', alpha=0.3, label='Winter')

    #   Tambahkan label dan judul
    ax4.set_xlabel('Month')
    ax4.set_ylabel('User Count')
    ax4.set_title('User Count per Month with Seasonal Background')
    ax4.legend()

    plt.xticks(rotation=45)

    # Tampilkan plot
    st.pyplot(fig4)

    st.write("Keterangan: warna background putih menandakan musim Spring")

    st.subheader("Bike Sharing Trend in 2012")
    # Kelompokkan data berdasarkan musim
    summer_2012 = df_2012[df_2012['season_mapped'] == 'Summer']
    fall_2012 = df_2012[df_2012['season_mapped'] == 'Fall']
    winter_2012 = df_2012[df_2012['season_mapped'] == 'Winter']
    spring_2012 = df_2012[df_2012['season_mapped'] == 'Spring']

    # Plot jumlah pengguna setiap bulannya
    fig5, ax5 = plt.subplots(figsize=(10, 6))
    ax5.plot(np.array(df_2012['month_mapped']), np.array(df_2012['count']), color='black', label='Total Users')

    # Tambahkan background untuk setiap musim
    ax5.fill_between(np.array(summer_2012['month_mapped']), np.array(summer_2012['count']), color='yellow', alpha=0.3, label='Summer')
    ax5.fill_between(np.array(fall_2012['month_mapped']), np.array(fall_2012['count']), color='orange', alpha=0.3, label='Fall')
    ax5.fill_between(np.array(winter_2012['month_mapped']), np.array(winter_2012['count']), color='blue', alpha=0.3, label='Winter')
    # plt.fill_between(spring_2012['month_mapped'], spring_2012['count'], color='green', alpha=0.3, label='Spring')

    # Tambahkan label dan judul
    ax5.set_xlabel('Month')
    ax5.set_ylabel('User Count')
    ax5.set_title('User Count per Month with Seasonal Background')
    ax5.legend()

    plt.xticks(rotation=45)

    # Tampilkan plot
    st.pyplot(fig5)

    st.write("Keterangan: warna background putih menandakan musim Spring")

st.caption('Copyright (c) Eldira Lahanny Permata Sherman 2024')
