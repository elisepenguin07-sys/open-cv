import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header("Airbnb site hotel")
df = pd.read_csv("Airbnb_site_hotel new.csv")

st.write("To understand which data are harder to collect, we will first identify the most challenging ones.")
df_na = df.isna().sum()
fig1, ax1 = plt.subplots()
ax1.barh(df_na.index, df_na.values, color='skyblue')
ax1.set_xlabel("Missing Data Columns")
ax1.tick_params(axis='x', rotation=75)
plt.tight_layout()
st.pyplot(fig1)

st.write("This chart displays the number of Airbnb listings in each city.")
fig2, ax2 = plt.subplots()
ax2.bar(df['city'].value_counts().index, df['city'].value_counts().values)
ax2.set_xlabel("City")
ax2.set_ylabel("Count")
ax2.set_title("Number of Listings per City")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig2)

