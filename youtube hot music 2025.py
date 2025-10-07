# data-analysis
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.header("YouTube Hot Music 2025")
df = pd.read_csv("youtube-top-100-songs-2025.csv")

st.subheader("Youtube Top 100 songs 2025")
st.write(df['title'])

fig, ax = plt.subplots()  # 建立 figure 和 axis
ax.scatter(df['duration'], df['view_count'])
ax.set_xlabel('Duration (seconds)')
ax.set_ylabel('View Count')
ax.set_title('View Count vs Duration')

st.pyplot(fig)
