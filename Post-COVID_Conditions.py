import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header("Post-COVID Conditions")
df = pd.read_csv("Post-COVID_Conditions.csv")

st.subheader("Missing Data")
st.write("To understand which data are harder to collect, we will first identify the most challenging ones.")
df_na = df.isna().sum()

fig1, ax1 = plt.subplots()
ax1.bar(df_na.index, df_na.values, color='skyblue')
ax1.set_xlabel("Missing Data Columns")
ax1.tick_params(axis='x', rotation=45)
st.pyplot(fig1)
