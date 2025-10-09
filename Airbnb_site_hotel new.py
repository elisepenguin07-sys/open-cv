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

st.write("This chart displays the average price in each city.")
df['city'] = pd.to_numeric(df['city'], errors='coerce')
df['city'] = df['city'].replace('[\$,]','',regex=True)
st.write(df['price'].describe())
#city_average_price = df.groupby('city')['price'].mean()
#fig3, ax3 = plt.subplots()
#ax3.bar(range(len(city_average_price)), city_average_price.values)
#ax3.set_xlabel("City")
#ax3.set_ylabel("price")
#ax3.set_title("Average price in each city")
#plt.tight_layout()
#st.pyplot(fig3)

