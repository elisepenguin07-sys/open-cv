# data-analysis
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.header("YouTube Hot Music 2025")
df = pd.read_csv("youtube-top-100-songs-2025.csv")

st.subheader("Youtube Top 100 songs 2025")
st.write(df['title'])

fig, ax = plt.subplots()  # 建立畫布和座標軸
ax.scatter(df['duration'], df['view_count'])  # 在座標軸上畫散點圖
ax.set_xlabel('Duration (seconds)')  # 設定 x 軸標籤
ax.set_ylabel('View Count')  # 設定 y 軸標籤
ax.set_title('View Count vs Duration')  # 設定圖表標題

st.pyplot(fig)
