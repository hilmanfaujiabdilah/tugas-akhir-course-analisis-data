import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="dark")

df = pd.read_csv("main_data.csv")

datetime_columns = ["dteday"]

for column in datetime_columns:
    df[column] = pd.to_datetime(df[column])

min_date = df["dteday"].min()
max_date = df["dteday"].max()

with st.sidebar:

    # Menambahkan logo perusahaan
    st.image("bike.png")

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label="Rentang Waktu",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date],
    )

main_df = df[(df["dteday"] >= str(start_date)) & (df["dteday"] <= str(end_date))]

st.header("DBike Dashboard :sparkles:")

st.subheader("Bike Sharing")

col1, col2 = st.columns(2)

with col1:
    sum_day_df = (
        main_df.groupby("workingday")
        .cnt.sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(20, 10))

    colors = ["#D3D3D3", "#90CAF9"]

    sns.barplot(
        y="cnt",
        x="workingday",
        data=sum_day_df.sort_values(by="workingday", ascending=False),
        palette=colors,
        ax=ax,
    )
    ax.set_title("Number of rentals based on working day", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    plt.xticks([0, 1], ["Bukan Hari Kerja", "Hari Kerja"])
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=30)
    st.pyplot(fig)

with col2:

    sum_day_df = (
        main_df.groupby("weathersit")
        .cnt.sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(20, 10))

    colors = ["#90CAF9", "#D3D3D3", "#D3D3D3"]

    sns.barplot(
        y="cnt",
        x="weathersit",
        data=sum_day_df.sort_values(by="weathersit", ascending=False),
        palette=colors,
        ax=ax,
    )
    ax.set_title("Number of rentals based on weather", loc="center", fontsize=50)
    plt.xticks([0, 1, 2], ["cerah", "berawan", "hujan"])
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=30)
    st.pyplot(fig)
