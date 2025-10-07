# data-analysis
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.header("YouTube Hot Music 2025")
df = pd.read_csv("youtube-top-100-songs-2025.csv")

st.subheader("Youtube Top 100 songs 2025")
st.write(df['title'])

plt.scatter(df['view_count'],df['duration'])
plt.xlabel("View count")
plt.ylabel("Duration(seconds)")
st.pyplot() 
