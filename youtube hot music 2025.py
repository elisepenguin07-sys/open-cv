# data-analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header("YouTube Hot Music 2025")
df = pd.read_csv("youtube-top-100-songs-2025.csv")

st.subheader("Youtube Top 100 songs 2025")
st.write(df['title'])

fig, ax = plt.subplots()  # 建立畫布和座標軸
ax.scatter(df['duration'], df['view_count'])  # 在座標軸上畫散點圖
ax.set_xlabel('Duration (seconds)')  
ax.set_ylabel('View Count') 
ax.set_title('View Count vs Duration') 
st.pyplot(fig)

fig2, ax2 = plt.subplots()
sns.boxplot(x='categories',y='view_count',data = df)
ax2.set_xlabel('Categorie')  
ax2.set_ylabel('View Count') 
ax2.set_title('View Count vs Categorie') 
st.pyplot(fig2)
