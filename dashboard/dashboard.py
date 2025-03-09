import pandas as pd

# import matplotlib.pyplot as plt
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
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label="Rentang Waktu",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date],
    )
